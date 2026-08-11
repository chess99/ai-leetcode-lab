from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from ai_leetcode.config import AttemptBudget
from ai_leetcode.events import EventStore
from ai_leetcode.stats import build_summary


class StatsTests(unittest.TestCase):
    def test_accepted_identity_falls_back_to_submission_start(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "archive").mkdir()
            (root / "archive" / "catalog.json").write_text(
                json.dumps(
                    {
                        "syncedAt": "2026-01-01T00:00:00Z",
                        "problems": [
                            {
                                "titleSlug": "two-sum",
                                "questionFrontendId": "1",
                                "difficulty": "EASY",
                                "paidOnly": False,
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            store = EventStore(root)
            store.append("problem_started", slug="two-sum")
            store.append(
                "submission_started",
                action_id="action-1",
                slug="two-sum",
                round=1,
                attempt=1,
                client="client-a",
                model="model-b",
            )
            # 兼容修复前的历史结果事件：身份只存在于对应的 started 事件中。
            store.append(
                "submission_result",
                action_id="action-1",
                slug="two-sum",
                round=1,
                attempt=1,
                outcome="accepted",
            )

            summary = build_summary(AttemptBudget(5, 3, 2, 0.01, 1), root=root)
            self.assertEqual(summary["acceptedByAgent"], {"client-a / model-b": 1})


if __name__ == "__main__":
    unittest.main()
