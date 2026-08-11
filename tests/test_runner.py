from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from ai_leetcode.client import JudgeTask
from ai_leetcode.config import ArchiveConfig, AttemptBudget, ExperimentConfig, Identity
from ai_leetcode.events import EventStore
from ai_leetcode.runner import submit_solution


class AcceptedClient:
    def __init__(self) -> None:
        self.submitted: dict[str, object] | None = None

    def submit_code(self, slug: str, question_id: int, language: str, code: str) -> JudgeTask:
        self.submitted = {
            "slug": slug,
            "question_id": question_id,
            "language": language,
            "code": code,
        }
        return JudgeTask("submission-123")

    def poll_judge(self, task_id: str):
        return {
            "state": "SUCCESS",
            "status_msg": "Accepted",
            "run_success": True,
            "total_correct": 63,
            "total_testcases": 63,
            "status_runtime": "1 ms",
        }


class RunnerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        problem = {
            "id": 1,
            "questionFrontendId": "1",
            "title": "Two Sum",
            "translatedTitle": "两数之和",
            "titleSlug": "two-sum",
            "difficulty": "EASY",
            "paidOnly": False,
        }
        (self.root / "archive").mkdir()
        (self.root / "archive" / "catalog.json").write_text(
            json.dumps({"problems": [problem]}), encoding="utf-8"
        )
        directory = self.root / "problems" / "0001-two-sum"
        directory.mkdir(parents=True)
        (directory / "solution.py").write_text("class Solution:\n    pass\n", encoding="utf-8")
        (directory / "meta.json").write_text(
            json.dumps(
                {
                    "questionId": "1",
                    "questionFrontendId": "1",
                    "titleSlug": "two-sum",
                    "language": "python3",
                    "solutionFile": "solution.py",
                }
            ),
            encoding="utf-8",
        )
        self.config = ExperimentConfig(
            "https://leetcode.cn",
            "python3",
            ArchiveConfig(100, 2, 0),
            AttemptBudget(5, 3, 2, 0.01, 1),
            True,
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_submit_records_judge_accepted(self) -> None:
        client = AcceptedClient()
        store = EventStore(self.root)
        event = submit_solution(
            "two-sum",
            client,  # type: ignore[arg-type]
            self.config,
            Identity("test-client", "test-model", "medium", "sol-medium"),
            store,
            root=self.root,
        )
        self.assertEqual(event["outcome"], "accepted")
        self.assertEqual(client.submitted["language"], "python3")  # type: ignore[index]
        self.assertEqual(store.usage("two-sum").submissions, 1)
        self.assertTrue(store.usage("two-sum").accepted)
        self.assertEqual(event["client"], "test-client")
        self.assertEqual(event["model"], "test-model")
        self.assertEqual(event["profile_id"], "sol-medium")
        self.assertEqual(event["reasoning_effort"], "medium")
        self.assertIn("remote_elapsed_ms", event)


if __name__ == "__main__":
    unittest.main()
