from __future__ import annotations

import unittest
from datetime import datetime, timezone

from ai_leetcode.quota import submission_quota_status


class SubmissionQuotaTests(unittest.TestCase):
    def test_waits_until_oldest_charged_submission_leaves_window(self) -> None:
        events = []
        for index in range(3):
            action_id = f"a-{index}"
            events.extend(
                [
                    {
                        "type": "submission_started",
                        "action_id": action_id,
                        "timestamp": f"2026-08-12T0{index}:00:00Z",
                    },
                    {
                        "type": "submission_result",
                        "action_id": action_id,
                        "outcome": "accepted",
                        "counts_against_budget": True,
                    },
                ]
            )
        status = submission_quota_status(
            events,
            limit=3,
            window_hours=24,
            buffer_seconds=15,
            now=datetime(2026, 8, 12, 12, tzinfo=timezone.utc),
        )
        self.assertEqual(status["used"], 3)
        self.assertEqual(status["waitSeconds"], 12 * 3600 + 15)
        self.assertEqual(status["nextAllowedAt"], "2026-08-13T00:00:15Z")

    def test_infrastructure_failure_does_not_consume_quota(self) -> None:
        events = [
            {
                "type": "submission_started",
                "action_id": "rate-limited",
                "timestamp": "2026-08-12T11:59:00Z",
            },
            {
                "type": "submission_result",
                "action_id": "rate-limited",
                "outcome": "infrastructure_error",
                "counts_against_budget": False,
            },
        ]
        status = submission_quota_status(
            events,
            limit=1,
            now=datetime(2026, 8, 12, 12, tzinfo=timezone.utc),
        )
        self.assertEqual(status["used"], 0)
        self.assertEqual(status["waitSeconds"], 0)

    def test_unfinished_submission_is_counted_conservatively(self) -> None:
        events = [
            {
                "type": "submission_started",
                "action_id": "unfinished",
                "timestamp": "2026-08-12T11:59:00Z",
            }
        ]
        status = submission_quota_status(
            events,
            limit=1,
            buffer_seconds=0,
            now=datetime(2026, 8, 12, 12, tzinfo=timezone.utc),
        )
        self.assertEqual(status["used"], 1)
        self.assertGreater(status["waitSeconds"], 0)


if __name__ == "__main__":
    unittest.main()
