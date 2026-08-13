from __future__ import annotations

import json
import hashlib
import os
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .config import AttemptBudget, Identity, ROOT, utc_now


class BudgetError(RuntimeError):
    """Raised when an action would exceed the experiment budget."""


@dataclass(frozen=True)
class Usage:
    round_number: int
    remote_tests: int
    submissions: int
    accepted: bool
    deferred: bool


class EventStore:
    def __init__(self, root: Path = ROOT):
        self.path = root / "data" / "attempts.jsonl"

    def load(self) -> list[dict[str, Any]]:
        if not self.path.exists():
            return []
        events: list[dict[str, Any]] = []
        for number, line in enumerate(self.path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"事件日志损坏：{self.path}:{number}: {exc}") from exc
            if not isinstance(event, dict):
                raise RuntimeError(f"事件日志不是对象：{self.path}:{number}")
            events.append(event)
        return events

    def append(self, event_type: str, **fields: Any) -> dict[str, Any]:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        event = {
            "event_id": str(uuid.uuid4()),
            "timestamp": utc_now(),
            "type": event_type,
            **fields,
        }
        line = json.dumps(event, ensure_ascii=False, separators=(",", ":")) + "\n"
        descriptor = os.open(self.path, os.O_WRONLY | os.O_APPEND | os.O_CREAT)
        try:
            os.write(descriptor, line.encode("utf-8"))
        finally:
            os.close(descriptor)
        return event

    def effective_events(self) -> list[dict[str, Any]]:
        """Return events with append-only annotations projected onto their targets."""
        events = self.load()
        known_ids = {str(event.get("event_id")) for event in events}
        patches: dict[str, dict[str, Any]] = {}
        for annotation in events:
            if annotation.get("type") != "profile_annotation":
                continue
            targets = annotation.get("target_event_ids") or annotation.get("targetEventIds") or []
            if not isinstance(targets, list):
                continue
            patch = {
                key: annotation[key]
                for key in ("profile_id", "client", "model", "reasoning_effort")
                if annotation.get(key) not in (None, "")
            }
            for target in targets:
                target_id = str(target)
                if target_id in known_ids:
                    patches.setdefault(target_id, {}).update(patch)
        for annotation in events:
            if annotation.get("type") != "result_annotation":
                continue
            target_id = str(
                annotation.get("target_event_id")
                or annotation.get("targetEventId")
                or ""
            )
            if target_id not in known_ids:
                continue
            patch = {
                key: annotation[key]
                for key in (
                    "outcome",
                    "counts_against_budget",
                    "remote_counts_against_quota",
                    "classification",
                )
                if key in annotation
            }
            patches.setdefault(target_id, {}).update(patch)
        return [
            {**event, **patches.get(str(event.get("event_id")), {})}
            if event.get("type") not in {"profile_annotation", "result_annotation"}
            else dict(event)
            for event in events
        ]

    def for_problem(self, slug: str) -> list[dict[str, Any]]:
        return [event for event in self.effective_events() if event.get("slug") == slug]

    def usage(self, slug: str, profile_id: str | None = None) -> Usage:
        events = self.for_problem(slug)
        profile_events = [
            event
            for event in events
            if profile_id is None or event.get("profile_id") == profile_id
        ]
        round_number = 1 + sum(
            1 for event in profile_events if event.get("type") == "retry_opened"
        )
        results_by_action = {
            event.get("action_id"): event
            for event in events
            if event.get("type") in {"remote_test_result", "submission_result"}
        }

        def charged_starts(kind: str) -> int:
            count = 0
            for event in profile_events:
                if event.get("type") != kind or int(event.get("round", 1)) != round_number:
                    continue
                result = results_by_action.get(event.get("action_id"))
                if result is None or result.get("counts_against_budget", True):
                    count += 1
            return count

        accepted = any(
            event.get("type") == "submission_result" and event.get("outcome") == "accepted"
            for event in events
        )
        deferred = False
        for event in profile_events:
            if event.get("type") == "profile_deferred":
                deferred = True
            elif event.get("type") == "profile_resumed":
                deferred = False
        return Usage(
            round_number=round_number,
            remote_tests=charged_starts("remote_test_started"),
            submissions=charged_starts("submission_started"),
            accepted=accepted,
            deferred=deferred,
        )

    def reserve_action(
        self,
        *,
        kind: str,
        problem: dict[str, Any],
        identity: Identity,
        language: str,
        code_hash: str,
        budget: AttemptBudget,
    ) -> dict[str, Any]:
        usage = self.usage(str(problem["titleSlug"]), identity.profile_id)
        if usage.accepted:
            raise BudgetError("该题已经 Accepted，不允许继续消耗远程尝试")
        if usage.deferred:
            raise BudgetError(f"该题已在 Profile {identity.profile_id} 标记为 defer")
        if usage.round_number > budget.max_rounds:
            raise BudgetError("该题已用完全部轮次")
        if kind == "remote_test":
            limit, used = budget.remote_tests_per_round, usage.remote_tests
        elif kind == "submission":
            limit, used = budget.submissions_per_round, usage.submissions
        else:
            raise ValueError(f"未知动作类型：{kind}")
        if used >= limit:
            label = "远程试跑" if kind == "remote_test" else "正式提交"
            raise BudgetError(f"第 {usage.round_number} 轮{label}预算已用完（{used}/{limit}）")
        action_id = str(uuid.uuid4())
        return self.append(
            f"{kind}_started",
            action_id=action_id,
            slug=problem["titleSlug"],
            question_id=str(problem.get("questionId") or problem.get("id")),
            frontend_id=str(problem.get("questionFrontendId", "")),
            round=usage.round_number,
            attempt=used + 1,
            language=language,
            client=identity.client,
            model=identity.model,
            reasoning_effort=identity.reasoning_effort,
            profile_id=identity.profile_id,
            code_sha256=code_hash,
        )

    def open_retry(self, slug: str, reason: str, budget: AttemptBudget, identity: Identity) -> dict[str, Any]:
        usage = self.usage(slug, identity.profile_id)
        if usage.accepted:
            raise BudgetError("该题已经 Accepted，无需开启重试轮")
        if usage.deferred:
            raise BudgetError(f"该题已在 Profile {identity.profile_id} 标记为 defer")
        if usage.round_number >= budget.max_rounds:
            raise BudgetError("该题已达到最大轮数")
        if usage.submissions < budget.submissions_per_round:
            raise BudgetError(
                f"当前轮正式提交尚未耗尽（{usage.submissions}/{budget.submissions_per_round}），不能提前重开"
            )
        if len(reason.strip()) < 10:
            raise BudgetError("重试原因至少 10 个字符，并应说明真正不同的新思路")
        return self.append(
            "retry_opened",
            slug=slug,
            from_round=usage.round_number,
            to_round=usage.round_number + 1,
            reason=reason.strip(),
            client=identity.client,
            model=identity.model,
            reasoning_effort=identity.reasoning_effort,
            profile_id=identity.profile_id,
        )

    def ensure_profile_started(
        self,
        problem: dict[str, Any],
        language: str,
        identity: Identity,
    ) -> dict[str, Any] | None:
        slug = str(problem["titleSlug"])
        events = self.for_problem(slug)
        if any(
            event.get("type") in {"problem_started", "profile_started"}
            and event.get("profile_id") == identity.profile_id
            for event in events
        ):
            return None
        if any(
            event.get("type") == "submission_result" and event.get("outcome") == "accepted"
            for event in events
        ):
            raise BudgetError("该题已经 Accepted，无需再为其他 Profile 开始作答")
        return self.append(
            "profile_started",
            slug=slug,
            question_id=str(problem.get("questionId") or problem.get("id", "")),
            frontend_id=str(problem.get("questionFrontendId", "")),
            language=language,
            client=identity.client,
            model=identity.model,
            reasoning_effort=identity.reasoning_effort,
            profile_id=identity.profile_id,
        )

    def defer_profile(self, slug: str, reason: str, identity: Identity) -> dict[str, Any]:
        if not any(
            event.get("type") in {"problem_started", "profile_started"}
            and event.get("profile_id") == identity.profile_id
            for event in self.for_problem(slug)
        ):
            raise BudgetError(f"请先用 Profile {identity.profile_id} start 该题，再执行 defer")
        usage = self.usage(slug, identity.profile_id)
        if usage.accepted:
            raise BudgetError("该题已经 Accepted，无需 defer")
        if usage.deferred:
            raise BudgetError(f"该题已在 Profile {identity.profile_id} 标记为 defer")
        if not reason.strip():
            raise BudgetError("defer 必须说明原因")
        return self.append(
            "profile_deferred",
            slug=slug,
            round=usage.round_number,
            remote_tests=usage.remote_tests,
            submissions=usage.submissions,
            reason=reason.strip(),
            client=identity.client,
            model=identity.model,
            reasoning_effort=identity.reasoning_effort,
            profile_id=identity.profile_id,
        )

    def resume_profile(self, slug: str, reason: str, identity: Identity) -> dict[str, Any]:
        usage = self.usage(slug, identity.profile_id)
        if usage.accepted:
            raise BudgetError("该题已经 Accepted，无需恢复 Profile")
        if not usage.deferred:
            raise BudgetError(f"该题在 Profile {identity.profile_id} 当前不是 defer 状态")
        if not reason.strip():
            raise BudgetError("恢复 Profile 必须说明依据")
        return self.append(
            "profile_resumed",
            slug=slug,
            reason=reason.strip(),
            client=identity.client,
            model=identity.model,
            reasoning_effort=identity.reasoning_effort,
            profile_id=identity.profile_id,
        )

    def annotate_profile(
        self,
        slug: str,
        target_event_ids: list[str],
        identity: Identity,
        reason: str,
    ) -> dict[str, Any]:
        raw_events = self.load()
        eligible = {
            str(event.get("event_id"))
            for event in raw_events
            if event.get("slug") == slug and event.get("type") != "profile_annotation"
        }
        targets = list(dict.fromkeys(str(item) for item in target_event_ids))
        missing = [item for item in targets if item not in eligible]
        if not targets:
            raise BudgetError("至少需要一个待校正的事件 ID")
        if missing:
            raise BudgetError(f"事件不属于题目 {slug} 或不存在：{', '.join(missing)}")
        if not reason.strip():
            raise BudgetError("历史校正必须说明依据")
        return self.append(
            "profile_annotation",
            slug=slug,
            target_event_ids=targets,
            profile_id=identity.profile_id,
            client=identity.client,
            model=identity.model,
            reasoning_effort=identity.reasoning_effort,
            reason=reason.strip(),
        )

    def annotate_result(
        self,
        slug: str,
        target_event_id: str,
        *,
        outcome: str,
        counts_against_budget: bool,
        classification: str,
        reason: str,
    ) -> dict[str, Any]:
        raw_events = self.load()
        target = next(
            (
                event
                for event in raw_events
                if str(event.get("event_id")) == str(target_event_id)
                and event.get("slug") == slug
                and event.get("type") in {"remote_test_result", "submission_result"}
            ),
            None,
        )
        if target is None:
            raise BudgetError(f"结果事件不属于题目 {slug} 或不存在：{target_event_id}")
        if outcome not in {"infrastructure_error", "failed", "rejected", "accepted"}:
            raise BudgetError(f"不支持的校正结果：{outcome}")
        if not classification.strip() or not reason.strip():
            raise BudgetError("结果校正必须提供分类与可核验依据")
        return self.append(
            "result_annotation",
            slug=slug,
            target_event_id=str(target_event_id),
            original_outcome=target.get("outcome"),
            outcome=outcome,
            counts_against_budget=bool(counts_against_budget),
            remote_counts_against_quota=bool(
                target.get("counts_against_budget", True)
            ),
            classification=classification.strip(),
            reason=reason.strip(),
        )

    def report_usage(
        self,
        slug: str,
        identity: Identity,
        *,
        source: str,
        input_tokens: int | None = None,
        output_tokens: int | None = None,
        cached_input_tokens: int | None = None,
        elapsed_seconds: float | None = None,
    ) -> dict[str, Any]:
        if not any(
            event.get("type") in {"problem_started", "profile_started"}
            and event.get("profile_id") == identity.profile_id
            for event in self.for_problem(slug)
        ):
            raise BudgetError(f"请先用 Profile {identity.profile_id} start 该题，再报告用量")
        values = (input_tokens, output_tokens, cached_input_tokens, elapsed_seconds)
        if all(value is None for value in values):
            raise BudgetError("至少报告一种 Token 用量或 elapsed_seconds")
        if any(value is not None and value < 0 for value in values):
            raise BudgetError("用量和耗时不能为负数")
        if not source.strip():
            raise BudgetError("用量报告必须注明可核验的数据来源")
        fields: dict[str, Any] = {
            "slug": slug,
            "source": source.strip(),
            "client": identity.client,
            "model": identity.model,
            "reasoning_effort": identity.reasoning_effort,
            "profile_id": identity.profile_id,
        }
        optional = {
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cached_input_tokens": cached_input_tokens,
            "elapsed_seconds": elapsed_seconds,
        }
        fields.update({key: value for key, value in optional.items() if value is not None})
        return self.append("usage_reported", **fields)

    def record_candidate_ready(
        self,
        *,
        problem: dict[str, Any],
        identity: Identity,
        language: str,
        code: str,
        validation: str,
        validation_level: str = "oracle",
    ) -> dict[str, Any]:
        slug = str(problem["titleSlug"])
        if not any(
            event.get("type") in {"problem_started", "profile_started"}
            and event.get("profile_id") == identity.profile_id
            for event in self.for_problem(slug)
        ):
            raise BudgetError(f"请先用 Profile {identity.profile_id} start 该题")
        if not validation.strip():
            raise BudgetError("候选验证记录不能为空")
        return self.append(
            "candidate_ready",
            slug=slug,
            question_id=str(problem.get("questionId") or problem.get("id", "")),
            frontend_id=str(problem.get("questionFrontendId", "")),
            language=language,
            code_sha256=hashlib.sha256(code.encode("utf-8")).hexdigest(),
            validation=validation.strip(),
            validation_level=validation_level,
            client=identity.client,
            model=identity.model,
            reasoning_effort=identity.reasoning_effort,
            profile_id=identity.profile_id,
        )

    def matching_candidate(
        self, slug: str, profile_id: str, code_sha256: str
    ) -> dict[str, Any] | None:
        latest = None
        for event in self.for_problem(slug):
            if (
                event.get("type") == "candidate_ready"
                and event.get("profile_id") == profile_id
            ):
                latest = event
        if latest is None or latest.get("code_sha256") != code_sha256:
            return None
        return latest
