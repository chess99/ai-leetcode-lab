from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from ai_leetcode.config import AttemptBudget, Identity
from ai_leetcode.events import BudgetError, EventStore


class EventBudgetTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.store = EventStore(self.root)
        self.budget = AttemptBudget(2, 2, 2, 0.01, 1)
        self.identity = Identity("test-client", "test-model", "medium", "sol-medium")
        self.problem = {"titleSlug": "two-sum", "id": 1, "questionFrontendId": "1"}

    def tearDown(self) -> None:
        self.temp.cleanup()

    def reserve_submission(self):
        return self.store.reserve_action(
            kind="submission",
            problem=self.problem,
            identity=self.identity,
            language="python3",
            code_hash="a" * 64,
            budget=self.budget,
        )

    def test_unfinished_action_conservatively_counts(self) -> None:
        self.reserve_submission()
        self.assertEqual(self.store.usage("two-sum").submissions, 1)
        self.assertEqual(self.store.usage("two-sum", "sol-medium").submissions, 1)
        self.assertEqual(self.store.usage("two-sum", "sol-high").submissions, 0)

    def test_infrastructure_failure_does_not_count_before_send(self) -> None:
        action = self.reserve_submission()
        self.store.append(
            "submission_result",
            action_id=action["action_id"],
            slug="two-sum",
            outcome="infrastructure_error",
            counts_against_budget=False,
        )
        self.assertEqual(self.store.usage("two-sum").submissions, 0)

    def test_retry_requires_exhausted_round_and_is_bounded(self) -> None:
        with self.assertRaises(BudgetError):
            self.store.open_retry("two-sum", "这是一个足够长的新思路", self.budget, self.identity)
        for _ in range(2):
            self.reserve_submission()
        event = self.store.open_retry("two-sum", "改用哈希表并检查所有边界情况", self.budget, self.identity)
        self.assertEqual(event["to_round"], 2)
        self.assertEqual(self.store.usage("two-sum").round_number, 2)
        with self.assertRaises(BudgetError):
            self.store.open_retry("two-sum", "再次尝试完全不同的算法方案", self.budget, self.identity)

    def test_defer_is_isolated_to_current_profile(self) -> None:
        self.store.ensure_profile_started(self.problem, "python3", self.identity)
        self.store.defer_profile("two-sum", "当前档位先跳过", self.identity)
        self.assertTrue(self.store.usage("two-sum", "sol-medium").deferred)
        self.assertFalse(self.store.usage("two-sum", "sol-high").deferred)
        with self.assertRaises(BudgetError):
            self.reserve_submission()

    def test_resume_reopens_deferred_profile_append_only(self) -> None:
        self.store.ensure_profile_started(self.problem, "python3", self.identity)
        self.store.defer_profile("two-sum", "当前档位先跳过", self.identity)
        event = self.store.resume_profile(
            "two-sum", "已经得到通过本地 oracle 的可靠候选", self.identity
        )
        self.assertEqual(event["type"], "profile_resumed")
        self.assertFalse(self.store.usage("two-sum", "sol-medium").deferred)
        self.reserve_submission()

    def test_profile_annotation_projects_without_rewriting_history(self) -> None:
        historical = self.store.append("problem_started", slug="two-sum", client="old", model="old")
        original = self.store.path.read_text(encoding="utf-8")
        self.store.annotate_profile(
            "two-sum",
            [historical["event_id"]],
            self.identity,
            "用户确认了当时运行配置",
        )
        effective = self.store.effective_events()[0]
        self.assertEqual(effective["profile_id"], "sol-medium")
        self.assertEqual(effective["model"], "test-model")
        self.assertTrue(self.store.path.read_text(encoding="utf-8").startswith(original))

    def test_result_annotation_reclassifies_without_rewriting_history(self) -> None:
        result = self.store.append(
            "submission_result",
            slug="two-sum",
            outcome="failed",
            counts_against_budget=True,
        )
        original = self.store.path.read_text(encoding="utf-8")
        annotation = self.store.annotate_result(
            "two-sum",
            result["event_id"],
            outcome="infrastructure_error",
            counts_against_budget=False,
            classification="submission_packaging_error",
            reason="判题器注入前缀使 future import 失去文件首行位置",
        )
        effective = self.store.effective_events()[0]
        self.assertEqual(annotation["type"], "result_annotation")
        self.assertEqual(effective["outcome"], "infrastructure_error")
        self.assertFalse(effective["counts_against_budget"])
        self.assertTrue(effective["remote_counts_against_quota"])
        self.assertEqual(effective["classification"], "submission_packaging_error")
        self.assertTrue(self.store.path.read_text(encoding="utf-8").startswith(original))

    def test_usage_report_requires_source_and_keeps_exact_values(self) -> None:
        self.store.ensure_profile_started(self.problem, "python3", self.identity)
        event = self.store.report_usage(
            "two-sum",
            self.identity,
            source="client usage API",
            input_tokens=120,
            output_tokens=30,
            elapsed_seconds=1.25,
        )
        self.assertEqual(event["input_tokens"], 120)
        self.assertNotIn("cached_input_tokens", event)

    def test_candidate_ready_records_profile_validation_and_code_hash(self) -> None:
        self.store.ensure_profile_started(self.problem, "python3", self.identity)
        event = self.store.record_candidate_ready(
            problem=self.problem,
            identity=self.identity,
            language="python3",
            code="class Solution:\n    pass\n",
            validation="题面样例与随机 oracle 通过",
        )
        self.assertEqual(event["type"], "candidate_ready")
        self.assertEqual(event["profile_id"], "sol-medium")
        self.assertEqual(len(event["code_sha256"]), 64)
        self.assertIn("oracle", event["validation"])
        self.assertEqual(event["validation_level"], "oracle")


if __name__ == "__main__":
    unittest.main()
