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
    def __init__(self, root: Path = ROOT, stale_seconds: int = 900):
        self.path = root / ".runtime" / "remote-action.lock"
        self.stale_seconds = stale_seconds
        self.acquired = False

    def __enter__(self) -> "RemoteActionLock":
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if self.path.exists():
            try:
                info = json.loads(self.path.read_text(encoding="utf-8"))
                age = time.time() - float(info.get("unixTime", 0))
            except (json.JSONDecodeError, OSError, ValueError, TypeError):
                age = 0
            if age <= self.stale_seconds:
                raise RuntimeError(f"已有远程动作在执行：{self.path}")
            self.path.unlink()
        descriptor = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        try:
            payload = json.dumps({"pid": os.getpid(), "unixTime": time.time(), "createdAt": utc_now()})
            os.write(descriptor, payload.encode("utf-8"))
        finally:
            os.close(descriptor)
        self.acquired = True
        return self

    def __exit__(self, exc_type: object, exc_value: object, traceback: object) -> None:
        if self.acquired and self.path.exists():
            self.path.unlink()
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

    with RemoteActionLock(root):
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
                remote_elapsed_ms=round((time.monotonic() - action_started) * 1000),
                judge_task_id=task.task_id,
                result=_safe_judge_result(actual),
                expected_result=_safe_judge_result(expected) if expected else None,
            )
        except ApiError as exc:
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
                remote_elapsed_ms=round((time.monotonic() - action_started) * 1000),
                error=str(exc),
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
    with RemoteActionLock(root):
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
                remote_elapsed_ms=round((time.monotonic() - action_started) * 1000),
                submission_id=task.task_id,
                result=_safe_judge_result(raw),
            )
        except ApiError as exc:
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
                remote_elapsed_ms=round((time.monotonic() - action_started) * 1000),
                error=str(exc),
            )
            raise
