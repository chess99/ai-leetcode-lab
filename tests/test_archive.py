from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from ai_leetcode.archive import materialize_problem, normalize_question, resolve_problem
from ai_leetcode.config import ArchiveConfig, AttemptBudget, ExperimentConfig, Identity
from ai_leetcode.events import EventStore


class ArchiveTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "archive").mkdir()
        self.problem = normalize_question(
            {
                "id": 1,
                "questionFrontendId": "1",
                "title": "Two Sum",
                "translatedTitle": "两数之和",
                "titleSlug": "two-sum",
                "difficulty": "EASY",
                "paidOnly": False,
                "topicTags": [{"name": "Array", "nameTranslated": "数组", "slug": "array"}],
            }
        )
        (self.root / "archive" / "catalog.json").write_text(
            json.dumps({"problems": [self.problem]}), encoding="utf-8"
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

    def test_resolve_by_slug_and_frontend_id(self) -> None:
        self.assertEqual(resolve_problem("two-sum", self.root)["id"], 1)
        self.assertEqual(resolve_problem("1", self.root)["titleSlug"], "two-sum")

    def test_materialize_writes_identity_and_template(self) -> None:
        detail = {
            "question": {
                "questionId": "1",
                "translatedContent": "<p>给定数组。</p>",
                "sampleTestCase": "[2,7]\n9",
                "topicTags": [{"translatedName": "数组"}],
                "codeSnippets": [{"langSlug": "python3", "code": "class Solution:\n    pass"}],
            }
        }
        directory = materialize_problem(
            self.problem,
            detail,
            self.config,
            Identity("client-a", "model-b", "high", "sol-high"),
            EventStore(self.root),
            language="python3",
            root=self.root,
        )
        solution = (directory / "solution.py").read_text(encoding="utf-8")
        self.assertIn("Client: client-a", solution)
        self.assertIn("Model: model-b", solution)
        self.assertIn("Reasoning effort: high", solution)
        self.assertIn("Profile: sol-high", solution)
        self.assertIn("class Solution", solution)
        self.assertEqual(len(EventStore(self.root).load()), 1)


if __name__ == "__main__":
    unittest.main()
