from __future__ import annotations

import hashlib
import json
import os
import time
from contextlib import AbstractContextManager
from pathlib import Path
from typing import Any

from .archive import ArchiveError, problem_key, resolve_problem
from .client import ApiError, LeetCodeClient
from .config import ExperimentConfig, Identity, ROOT, atomic_write_json, utc_now
from .events import EventStore


RESULT_FIELDS = (
    "state",
    "status_code",
    "status_msg",
    "run_success",
    "total_correct",
    "total_testcases",
    "status_runtime",
    "status_memory",
    "input",
    "last_testcase",
    "code_answer",
    "code_output",
    "expected_output",
    "std_output",
    "compile_error",
    "runtime_error",
    "full_runtime_error",
)


class RemoteActionLock(AbstractContextManager["RemoteActionLock"]):
    def __init__(
        self,
        root: Path = ROOT,
        stale_seconds: int = 900,
        wait_seconds: float = 300,
        poll_seconds: float = 0.2,
        min_interval_seconds: float = 13.0,
    ):
        self.path = root / ".runtime" / "remote-action.lock"
        self.last_action_path = root / ".runtime" / "last-remote-action.json"
        self.backoff_path = root / ".runtime" / "remote-backoff.json"
        self.stale_seconds = stale_seconds
        self.wait_seconds = wait_seconds
        self.poll_seconds = poll_seconds
        self.min_interval_seconds = min_interval_seconds
        self.acquired = False

    def _unlink_with_retry(self, timeout_seconds: float = 1.0) -> bool:
        deadline = time.monotonic() + timeout_seconds
        while True:
            try:
                self.path.unlink()
                return True
            except FileNotFoundError:
                return True
            except PermissionError:
                if time.monotonic() >= deadline:
                    return False
                time.sleep(min(self.poll_seconds, 0.05))

    def __enter__(self) -> "RemoteActionLock":
        self.path.parent.mkdir(parents=True, exist_ok=True)
        deadline = time.monotonic() + self.wait_seconds
        while True:
            if self.path.exists():
                try:
                    age = time.time() - self.path.stat().st_mtime
                except FileNotFoundError:
                    continue
                except OSError:
                    age = 0
                if age > self.stale_seconds:
                    if not self._unlink_with_retry():
                        if time.monotonic() >= deadline:
                            raise RuntimeError(f"清理远程动作锁超时：{self.path}")
                        time.sleep(self.poll_seconds)
                        continue
                else:
                    if time.monotonic() >= deadline:
                        raise RuntimeError(f"等待远程动作锁超时：{self.path}")
                    time.sleep(self.poll_seconds)
                    continue
            try:
                descriptor = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            except FileExistsError:
                if time.monotonic() >= deadline:
                    raise RuntimeError(f"等待远程动作锁超时：{self.path}")
                time.sleep(self.poll_seconds)
                continue
            try:
                payload = json.dumps(
                    {"pid": os.getpid(), "unixTime": time.time(), "createdAt": utc_now()}
                )
                os.write(descriptor, payload.encode("utf-8"))
            finally:
                os.close(descriptor)
            try:
                backoff = json.loads(self.backoff_path.read_text(encoding="utf-8"))
                backoff_seconds = float(backoff.get("untilUnix", 0)) - time.time()
            except (FileNotFoundError, json.JSONDecodeError, OSError, TypeError, ValueError):
                backoff_seconds = 0
            if backoff_seconds > 0:
                time.sleep(backoff_seconds)
            try:
                previous = json.loads(self.last_action_path.read_text(encoding="utf-8"))
                since_previous = time.time() - float(previous.get("unixTime", 0))
            except (FileNotFoundError, json.JSONDecodeError, OSError, TypeError, ValueError):
                since_previous = self.min_interval_seconds
            cooldown = self.min_interval_seconds - since_previous
            if cooldown > 0:
                time.sleep(cooldown)
            atomic_write_json(
                self.last_action_path,
                {"unixTime": time.time(), "startedAt": utc_now()},
            )
            self.acquired = True
            return self

    def register_backoff(self, seconds: float = 60, max_seconds: float = 900) -> float:
        now = time.time()
        consecutive_429 = 1
        try:
            previous = json.loads(self.backoff_path.read_text(encoding="utf-8"))
            registered_unix = float(
                previous.get("registeredUnix")
                or (
                    float(previous.get("untilUnix", 0))
                    - float(previous.get("delaySeconds", 30))
                )
            )
            if (
                previous.get("reason") == "LeetCode HTTP 429"
                and now - registered_unix < 3600
            ):
                consecutive_429 = int(previous.get("consecutive429", 1)) + 1
        except (FileNotFoundError, json.JSONDecodeError, OSError, TypeError, ValueError):
            pass
        delay_seconds = min(seconds * (2 ** (consecutive_429 - 1)), max_seconds)
        atomic_write_json(
            self.backoff_path,
            {
                "untilUnix": now + delay_seconds,
                "registeredAt": utc_now(),
                "registeredUnix": now,
                "reason": "LeetCode HTTP 429",
                "consecutive429": consecutive_429,
                "delaySeconds": delay_seconds,
            },
        )
        return delay_seconds

    def clear_backoff(self) -> None:
        try:
            self.backoff_path.unlink()
        except FileNotFoundError:
            pass

    def __exit__(self, exc_type: object, exc_value: object, traceback: object) -> None:
        try:
            if self.acquired and not self._unlink_with_retry():
                raise RuntimeError(f"释放远程动作锁超时：{self.path}")
        finally:
            self.acquired = False


def _working_problem(selector: str, root: Path) -> tuple[dict[str, Any], dict[str, Any], Path, str]:
    problem = resolve_problem(selector, root)
    directory = root / "problems" / problem_key(problem)
    meta_path = directory / "meta.json"
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ArchiveError(f"该题尚未 start：{problem['titleSlug']}") from exc
    solution_path = directory / str(meta.get("solutionFile", ""))
    try:
        code = solution_path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise ArchiveError(f"解答文件不存在：{solution_path}") from exc
    return problem, meta, solution_path, code


def _safe_judge_result(raw: dict[str, Any]) -> dict[str, Any]:
    return {key: raw[key] for key in RESULT_FIELDS if key in raw and raw[key] not in (None, "")}


def _judge_errors(raw: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in ("compile_error", "runtime_error", "full_runtime_error"):
        value = raw.get(key)
        if value:
            errors.append(str(value))
    return errors


def run_remote_test(
    selector: str,
    test_input: str | None,
    client: LeetCodeClient,
    config: ExperimentConfig,
    identity: Identity,
    events: EventStore,
    *,
    root: Path = ROOT,
) -> dict[str, Any]:
    problem, meta, _, code = _working_problem(selector, root)
    code_hash = hashlib.sha256(code.encode("utf-8")).hexdigest()
    language = str(meta["language"])
    sample = test_input
    if sample is None:
        from .archive import load_detail

        sample = str((load_detail(problem, root).get("question") or {}).get("sampleTestCase") or "")
    if not sample:
        raise ArchiveError("缺少测试输入；请使用 --input 或 --input-file")

    with RemoteActionLock(root) as remote_lock:
        working_problem = {**problem, "questionId": meta["questionId"]}
        events.ensure_profile_started(working_problem, language, identity)
        reservation = events.reserve_action(
            kind="remote_test",
            problem=working_problem,
            identity=identity,
            language=language,
            code_hash=code_hash,
            budget=config.attempt_budget,
        )
        task_sent = False
        action_started = time.monotonic()
        try:
            task = client.run_code(str(problem["titleSlug"]), int(meta["questionId"]), language, code, sample)
            task_sent = True
            actual = client.poll_judge(task.task_id)
            expected = client.poll_judge(task.expected_id) if task.expected_id else None
            remote_lock.clear_backoff()
            no_errors = not _judge_errors(actual)
            outputs_match = expected is None or actual.get("code_answer") == expected.get("code_answer")
            passed = bool(actual.get("run_success")) and no_errors and outputs_match
            return events.append(
                "remote_test_result",
                action_id=reservation["action_id"],
                slug=problem["titleSlug"],
                round=reservation["round"],
                attempt=reservation["attempt"],
                outcome="passed" if passed else "failed",
                counts_against_budget=True,
                client=identity.client,
                model=identity.model,
                reasoning_effort=identity.reasoning_effort,
                profile_id=identity.profile_id,
                code_sha256=code_hash,
                remote_elapsed_ms=round((time.monotonic() - action_started) * 1000),
                judge_task_id=task.task_id,
                result=_safe_judge_result(actual),
                expected_result=_safe_judge_result(expected) if expected else None,
            )
        except ApiError as exc:
            backoff_seconds = None
            if "HTTP 429" in str(exc):
                backoff_seconds = remote_lock.register_backoff()
            events.append(
                "remote_test_result",
                action_id=reservation["action_id"],
                slug=problem["titleSlug"],
                round=reservation["round"],
                attempt=reservation["attempt"],
                outcome="infrastructure_error" if exc.infrastructure or exc.authentication else "rejected",
                counts_against_budget=task_sent or not (exc.infrastructure or exc.authentication),
                client=identity.client,
                model=identity.model,
                reasoning_effort=identity.reasoning_effort,
                profile_id=identity.profile_id,
                code_sha256=code_hash,
                remote_elapsed_ms=round((time.monotonic() - action_started) * 1000),
                error=str(exc),
                backoff_seconds=backoff_seconds,
            )
            raise


def submit_solution(
    selector: str,
    client: LeetCodeClient,
    config: ExperimentConfig,
    identity: Identity,
    events: EventStore,
    *,
    root: Path = ROOT,
) -> dict[str, Any]:
    problem, meta, _, code = _working_problem(selector, root)
    code_hash = hashlib.sha256(code.encode("utf-8")).hexdigest()
    language = str(meta["language"])
    if events.matching_candidate(str(problem["titleSlug"]), identity.profile_id, code_hash) is None:
        raise ArchiveError(
            f"当前代码没有匹配 Profile {identity.profile_id} 的 candidate-ready 哈希；"
            "请先完成本地验证并记录候选"
        )
    with RemoteActionLock(root) as remote_lock:
        working_problem = {**problem, "questionId": meta["questionId"]}
        events.ensure_profile_started(working_problem, language, identity)
        reservation = events.reserve_action(
            kind="submission",
            problem=working_problem,
            identity=identity,
            language=language,
            code_hash=code_hash,
            budget=config.attempt_budget,
        )
        task_sent = False
        action_started = time.monotonic()
        try:
            task = client.submit_code(str(problem["titleSlug"]), int(meta["questionId"]), language, code)
            task_sent = True
            raw = client.poll_judge(task.task_id)
            remote_lock.clear_backoff()
            status = str(raw.get("status_msg") or "")
            accepted = status == "Accepted" and bool(raw.get("run_success", True))
            return events.append(
                "submission_result",
                action_id=reservation["action_id"],
                slug=problem["titleSlug"],
                round=reservation["round"],
                attempt=reservation["attempt"],
                outcome="accepted" if accepted else "failed",
                counts_against_budget=True,
                client=identity.client,
                model=identity.model,
                reasoning_effort=identity.reasoning_effort,
                profile_id=identity.profile_id,
                code_sha256=code_hash,
                remote_elapsed_ms=round((time.monotonic() - action_started) * 1000),
                submission_id=task.task_id,
                result=_safe_judge_result(raw),
            )
        except ApiError as exc:
            backoff_seconds = None
            if "HTTP 429" in str(exc):
                backoff_seconds = remote_lock.register_backoff()
            events.append(
                "submission_result",
                action_id=reservation["action_id"],
                slug=problem["titleSlug"],
                round=reservation["round"],
                attempt=reservation["attempt"],
                outcome="infrastructure_error" if exc.infrastructure or exc.authentication else "rejected",
                counts_against_budget=task_sent or not (exc.infrastructure or exc.authentication),
                client=identity.client,
                model=identity.model,
                reasoning_effort=identity.reasoning_effort,
                profile_id=identity.profile_id,
                code_sha256=code_hash,
                remote_elapsed_ms=round((time.monotonic() - action_started) * 1000),
                error=str(exc),
                backoff_seconds=backoff_seconds,
            )
            raise
