from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from ai_leetcode.config import AttemptBudget
from ai_leetcode.events import EventStore
from ai_leetcode.stats import build_summary


class StatsTests(unittest.TestCase):
    @staticmethod
    def write_profiles(root: Path) -> None:
        (root / "config").mkdir()
        (root / "config" / "profiles.json").write_text(
            json.dumps(
                {
                    "defaultProfile": "sol-medium",
                    "executionLadder": ["sol-medium", "sol-high"],
                    "profiles": [
                        {
                            "id": "sol-medium",
                            "model": "gpt-5.6-sol",
                            "reasoningEffort": "medium",
                            "cohort": "sol-escalation",
                            "stage": 1,
                            "enabled": True,
                        },
                        {
                            "id": "sol-high",
                            "model": "gpt-5.6-sol",
                            "reasoningEffort": "high",
                            "cohort": "sol-escalation",
                            "stage": 2,
                            "enabled": True,
                        },
                    ],
                }
            ),
            encoding="utf-8",
        )

    def test_accepted_identity_falls_back_to_submission_start(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_profiles(root)
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
            self.assertEqual(summary["acceptedByProfile"], {"unprofiled": 1})
            self.assertEqual(summary["byDifficulty"]["EASY"]["eligible"], 1)

    def test_summary_attributes_first_success_and_token_coverage_to_profile(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_profiles(root)
            (root / "archive").mkdir()
            (root / "archive" / "catalog.json").write_text(
                json.dumps(
                    {
                        "problems": [
                            {
                                "titleSlug": "two-sum",
                                "questionFrontendId": "1",
                                "difficulty": "EASY",
                                "paidOnly": False,
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            store = EventStore(root)
            identity = {
                "client": "Codex Desktop",
                "model": "gpt-5.6-sol",
                "reasoning_effort": "medium",
                "profile_id": "sol-medium",
            }
            store.append("problem_started", slug="two-sum", **identity)
            store.append(
                "submission_started",
                action_id="a1",
                slug="two-sum",
                round=1,
                attempt=1,
                **identity,
            )
            store.append(
                "submission_result",
                action_id="a1",
                slug="two-sum",
                round=1,
                attempt=1,
                outcome="accepted",
                **identity,
            )
            store.append(
                "usage_reported",
                slug="two-sum",
                source="client usage API",
                input_tokens=100,
                output_tokens=20,
                **identity,
            )
            store.append(
                "candidate_ready",
                slug="two-sum",
                code_sha256="a" * 64,
                validation="oracle passed",
                **identity,
            )

            summary = build_summary(AttemptBudget(5, 3, 2, 0.01, 1), root=root)
            self.assertEqual(summary["acceptedByProfile"], {"sol-medium": 1})
            self.assertEqual(summary["firstSuccessByDifficulty"]["EASY"], {"sol-medium": 1})
            capability = summary["capabilityByDifficulty"]
            self.assertEqual(capability["difficultyOrder"], ["EASY"])
            self.assertEqual(
                capability["rows"],
                [
                    {
                        "kind": "firstAccepted",
                        "profileId": "sol-medium",
                        "model": "gpt-5.6-sol",
                        "reasoningEffort": "medium",
                        "byDifficulty": {"EASY": 1},
                        "total": 1,
                    },
                    {
                        "kind": "firstAccepted",
                        "profileId": "sol-high",
                        "model": "gpt-5.6-sol",
                        "reasoningEffort": "high",
                        "byDifficulty": {"EASY": 0},
                        "total": 0,
                    },
                    {
                        "kind": "pendingInLadder",
                        "profileId": None,
                        "model": None,
                        "reasoningEffort": None,
                        "byDifficulty": {"EASY": 0},
                        "total": 0,
                    },
                ],
            )
            self.assertTrue(capability["isComplete"])
            self.assertEqual(capability["accountedByDifficulty"], {"EASY": 1})
            self.assertEqual(
                capability["byProblem"]["two-sum"],
                {
                    "frontendId": "1",
                    "difficulty": "EASY",
                    "kind": "firstAccepted",
                    "profileId": "sol-medium",
                    "model": "gpt-5.6-sol",
                    "reasoningEffort": "medium",
                },
            )
            self.assertEqual(
                summary["firstSuccessByProblem"]["two-sum"]["profileId"], "sol-medium"
            )
            self.assertEqual(summary["profiles"]["sol-medium"]["usage"]["inputTokens"], 100)
            self.assertEqual(summary["profiles"]["sol-medium"]["candidateReady"], 1)
            self.assertEqual(summary["candidateReady"], 1)
            self.assertEqual(
                summary["ladderPaths"]["two-sum"][0]["candidateReady"], True
            )
            self.assertEqual(summary["candidateCodeDrift"], [])
            self.assertEqual(summary["usageCoverage"]["coverage"], 1.0)

    def test_accepted_code_drift_distinguishes_a_recorded_current_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_profiles(root)
            (root / "archive").mkdir()
            (root / "archive" / "catalog.json").write_text(
                json.dumps(
                    {
                        "problems": [
                            {
                                "id": 1,
                                "titleSlug": "two-sum",
                                "questionFrontendId": "1",
                                "difficulty": "EASY",
                                "paidOnly": False,
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            problem_dir = root / "problems" / "0001-two-sum"
            problem_dir.mkdir(parents=True)
            (problem_dir / "meta.json").write_text(
                json.dumps({"solutionFile": "solution.py"}), encoding="utf-8"
            )
            accepted_code = "class Solution:\n    pass\n"
            current_code = "class Solution:\n    answer = 42\n"
            (problem_dir / "solution.py").write_text(current_code, encoding="utf-8")

            identity = {
                "client": "Codex Desktop",
                "model": "gpt-5.6-sol",
                "reasoning_effort": "medium",
                "profile_id": "sol-medium",
            }
            store = EventStore(root)
            store.append("problem_started", slug="two-sum", **identity)
            store.append(
                "submission_started",
                action_id="submit-1",
                slug="two-sum",
                code_sha256=hashlib.sha256(accepted_code.encode()).hexdigest(),
                **identity,
            )
            store.append(
                "submission_result",
                action_id="submit-1",
                slug="two-sum",
                outcome="accepted",
                **identity,
            )
            store.append(
                "candidate_ready",
                slug="two-sum",
                code_sha256=hashlib.sha256(current_code.encode()).hexdigest(),
                **identity,
            )

            summary = build_summary(AttemptBudget(5, 3, 2, 0.01, 1), root=root)
            self.assertEqual(len(summary["acceptedCodeDrift"]), 1)
            self.assertEqual(summary["acceptedCodeExactMatchCount"], 0)
            self.assertTrue(summary["acceptedCodeDrift"][0]["currentCandidateRecorded"])
            self.assertEqual(summary["candidateCodeDrift"], [])

    def test_infrastructure_failures_do_not_lower_submission_acceptance_rate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_profiles(root)
            (root / "archive").mkdir()
            (root / "archive" / "catalog.json").write_text(
                json.dumps(
                    {
                        "problems": [
                            {
                                "titleSlug": "two-sum",
                                "questionFrontendId": "1",
                                "difficulty": "EASY",
                                "paidOnly": False,
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            store = EventStore(root)
            identity = {
                "client": "Codex Desktop",
                "model": "gpt-5.6-sol",
                "reasoning_effort": "medium",
                "profile_id": "sol-medium",
            }
            store.append("problem_started", slug="two-sum", **identity)
            store.append(
                "remote_test_started", action_id="test-429", slug="two-sum", **identity
            )
            store.append(
                "remote_test_result",
                action_id="test-429",
                slug="two-sum",
                outcome="infrastructure_error",
                counts_against_budget=False,
                **identity,
            )
            store.append(
                "submission_started", action_id="submit-429", slug="two-sum", **identity
            )
            store.append(
                "submission_result",
                action_id="submit-429",
                slug="two-sum",
                outcome="infrastructure_error",
                counts_against_budget=False,
                **identity,
            )
            store.append(
                "submission_started", action_id="submit-ok", slug="two-sum", **identity
            )
            store.append(
                "submission_result",
                action_id="submit-ok",
                slug="two-sum",
                outcome="accepted",
                **identity,
            )

            summary = build_summary(AttemptBudget(5, 3, 2, 0.01, 1), root=root)
            self.assertEqual(summary["remoteTests"], 0)
            self.assertEqual(summary["submissions"], 1)
            self.assertEqual(summary["overallSubmissionAcceptanceRate"], 1.0)
            self.assertEqual(summary["profiles"]["sol-medium"]["remoteTests"], 0)
            self.assertEqual(summary["profiles"]["sol-medium"]["submissions"], 1)
            self.assertEqual(summary["profiles"]["sol-medium"]["failedSubmissions"], 0)
            self.assertEqual(
                summary["infrastructureErrors"],
                {
                    "remoteTests": 1,
                    "submissions": 1,
                    "total": 2,
                    "countsAgainstModelMetrics": False,
                },
            )
            self.assertEqual(
                summary["profiles"]["sol-medium"]["infrastructureErrors"],
                {"remoteTests": 1, "submissions": 1},
            )

    def test_free_difficulty_denominator_excludes_paid_and_reports_pending(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_profiles(root)
            (root / "archive").mkdir()
            (root / "archive" / "catalog.json").write_text(
                json.dumps(
                    {
                        "problems": [
                            {
                                "titleSlug": "free-easy",
                                "questionFrontendId": "1",
                                "difficulty": "EASY",
                                "paidOnly": False,
                            },
                            {
                                "titleSlug": "paid-easy",
                                "questionFrontendId": "2",
                                "difficulty": "EASY",
                                "paidOnly": True,
                            },
                        ]
                    }
                ),
                encoding="utf-8",
            )
            store = EventStore(root)
            store.append(
                "problem_started",
                slug="free-easy",
                profile_id="sol-medium",
            )

            summary = build_summary(AttemptBudget(5, 3, 2, 0.01, 1), root=root)
            self.assertEqual(summary["catalogByDifficulty"]["EASY"], {"all": 2, "free": 1, "paid": 1})
            self.assertEqual(summary["byDifficulty"]["EASY"]["eligible"], 1)
            self.assertEqual(
                summary["experimentByDifficulty"]["EASY"]["awaitingRemoteAccepted"], 1
            )
            self.assertEqual(summary["awaitingRemoteAccepted"], 1)
            capability = summary["capabilityByDifficulty"]
            self.assertFalse(capability["isComplete"])
            self.assertEqual(capability["pending"], 1)
            self.assertEqual(capability["accountedByDifficulty"], {"EASY": 1})
            self.assertEqual(
                [row for row in capability["rows"] if row["kind"] == "pendingInLadder"],
                [
                    {
                        "kind": "pendingInLadder",
                        "profileId": None,
                        "model": None,
                        "reasoningEffort": None,
                        "byDifficulty": {"EASY": 1},
                        "total": 1,
                    }
                ],
            )
            self.assertEqual(
                capability["byProblem"]["free-easy"],
                {
                    "frontendId": "1",
                    "difficulty": "EASY",
                    "kind": "pendingInLadder",
                    "profileId": None,
                    "model": None,
                    "reasoningEffort": None,
                },
            )
            self.assertNotIn("paid-easy", capability["byProblem"])

    def test_defer_populates_next_profile_escalation_queue(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_profiles(root)
            (root / "archive").mkdir()
            (root / "archive" / "catalog.json").write_text(
                json.dumps(
                    {
                        "problems": [
                            {
                                "titleSlug": "hard-one",
                                "questionFrontendId": "99",
                                "difficulty": "HARD",
                                "paidOnly": False,
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            store = EventStore(root)
            store.append("problem_started", slug="hard-one", profile_id="sol-medium")
            store.append("profile_deferred", slug="hard-one", profile_id="sol-medium")

            summary = build_summary(AttemptBudget(5, 3, 2, 0.01, 1), root=root)
            item = summary["escalationQueueByProfile"]["sol-high"][0]
            self.assertEqual(item["slug"], "hard-one")
            self.assertTrue(item["needsNewCandidate"])

    def test_execution_ladder_escalates_across_model_cohorts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "config").mkdir()
            (root / "config" / "profiles.json").write_text(
                json.dumps(
                    {
                        "defaultProfile": "sol-medium",
                        "executionLadder": ["terra-medium", "sol-medium"],
                        "profiles": [
                            {
                                "id": "terra-medium",
                                "model": "gpt-5.6-terra",
                                "reasoningEffort": "medium",
                                "cohort": "terra-control",
                                "stage": 1,
                                "enabled": True,
                            },
                            {
                                "id": "sol-medium",
                                "model": "gpt-5.6-sol",
                                "reasoningEffort": "medium",
                                "cohort": "sol-escalation",
                                "stage": 1,
                                "enabled": True,
                            },
                        ],
                    }
                ),
                encoding="utf-8",
            )
            (root / "archive").mkdir()
            (root / "archive" / "catalog.json").write_text(
                json.dumps(
                    {
                        "problems": [
                            {
                                "titleSlug": "hard-one",
                                "questionFrontendId": "99",
                                "difficulty": "HARD",
                                "paidOnly": False,
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            store = EventStore(root)
            store.append("problem_started", slug="hard-one", profile_id="terra-medium")
            store.append("profile_deferred", slug="hard-one", profile_id="terra-medium")

            summary = build_summary(AttemptBudget(5, 3, 2, 0.01, 1), root=root)
            self.assertEqual(summary["executionLadder"], ["terra-medium", "sol-medium"])
            self.assertEqual(
                summary["escalationQueueByProfile"]["sol-medium"][0]["slug"],
                "hard-one",
            )
            self.assertEqual(summary["unresolvedAtHighestProfile"], [])

    def test_escalation_queue_does_not_duplicate_completed_historical_edges(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_profiles(root)
            (root / "archive").mkdir()
            (root / "archive" / "catalog.json").write_text(
                json.dumps(
                    {
                        "problems": [
                            {
                                "titleSlug": "hard-one",
                                "questionFrontendId": "99",
                                "difficulty": "HARD",
                                "paidOnly": False,
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            store = EventStore(root)
            for profile_id in ("sol-medium", "sol-high"):
                store.append("profile_started", slug="hard-one", profile_id=profile_id)
                store.append("profile_deferred", slug="hard-one", profile_id=profile_id)

            summary = build_summary(AttemptBudget(5, 3, 2, 0.01, 1), root=root)
            self.assertEqual(summary["escalationQueueByProfile"]["sol-high"], [])
            self.assertEqual(
                summary["unresolvedAtHighestProfile"],
                [{"profileId": "sol-high", "slug": "hard-one"}],
            )
            capability = summary["capabilityByDifficulty"]
            self.assertTrue(capability["isComplete"])
            self.assertEqual(capability["pending"], 0)
            self.assertEqual(capability["accountedByDifficulty"], {"HARD": 1})
            self.assertEqual(
                [row for row in capability["rows"] if row["kind"] == "highestUnresolved"],
                [
                    {
                        "kind": "highestUnresolved",
                        "profileId": "sol-high",
                        "model": "gpt-5.6-sol",
                        "reasoningEffort": "high",
                        "byDifficulty": {"HARD": 1},
                        "total": 1,
                    }
                ],
            )
            self.assertEqual(
                capability["byProblem"]["hard-one"],
                {
                    "frontendId": "99",
                    "difficulty": "HARD",
                    "kind": "highestUnresolved",
                    "profileId": "sol-high",
                    "model": "gpt-5.6-sol",
                    "reasoningEffort": "high",
                },
            )


if __name__ == "__main__":
    unittest.main()
