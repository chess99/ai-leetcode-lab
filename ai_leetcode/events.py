from __future__ import annotations

import json
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

    def for_problem(self, slug: str) -> list[dict[str, Any]]:
        return [event for event in self.load() if event.get("slug") == slug]

    def usage(self, slug: str) -> Usage:
        events = self.for_problem(slug)
        round_number = 1 + sum(1 for event in events if event.get("type") == "retry_opened")
        results_by_action = {
            event.get("action_id"): event
            for event in events
            if event.get("type") in {"remote_test_result", "submission_result"}
        }

        def charged_starts(kind: str) -> int:
            count = 0
            for event in events:
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
        return Usage(
            round_number=round_number,
            remote_tests=charged_starts("remote_test_started"),
            submissions=charged_starts("submission_started"),
            accepted=accepted,
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
        usage = self.usage(str(problem["titleSlug"]))
        if usage.accepted:
            raise BudgetError("该题已经 Accepted，不允许继续消耗远程尝试")
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
            code_sha256=code_hash,
        )

    def open_retry(self, slug: str, reason: str, budget: AttemptBudget, identity: Identity) -> dict[str, Any]:
        usage = self.usage(slug)
        if usage.accepted:
            raise BudgetError("该题已经 Accepted，无需开启重试轮")
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
        )
