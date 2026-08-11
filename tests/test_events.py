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
        self.identity = Identity("test-client", "test-model")
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


if __name__ == "__main__":
    unittest.main()
