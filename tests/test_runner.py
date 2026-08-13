from __future__ import annotations

import json
import hashlib
import tempfile
import threading
import time
import unittest
from pathlib import Path
from unittest.mock import patch

from ai_leetcode.client import JudgeTask
from ai_leetcode.config import ArchiveConfig, AttemptBudget, ExperimentConfig, Identity
from ai_leetcode.events import EventStore
from ai_leetcode.runner import RemoteActionLock, submit_solution


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
        store.ensure_profile_started(
            {"titleSlug": "two-sum", "id": 1, "questionFrontendId": "1"},
            "python3",
            Identity("test-client", "test-model", "medium", "sol-medium"),
        )
        store.record_candidate_ready(
            problem={"titleSlug": "two-sum", "id": 1, "questionFrontendId": "1"},
            identity=Identity("test-client", "test-model", "medium", "sol-medium"),
            language="python3",
            code="class Solution:\n    pass\n",
            validation="unit test",
        )
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
        self.assertEqual(
            event["code_sha256"],
            hashlib.sha256("class Solution:\n    pass\n".encode()).hexdigest(),
        )

    def test_submit_rejects_code_without_matching_candidate_hash(self) -> None:
        with self.assertRaisesRegex(Exception, "candidate-ready"):
            submit_solution(
                "two-sum",
                AcceptedClient(),  # type: ignore[arg-type]
                self.config,
                Identity("test-client", "test-model", "medium", "sol-medium"),
                EventStore(self.root),
                root=self.root,
            )

    def test_remote_lock_queues_parallel_workers(self) -> None:
        first = RemoteActionLock(
            self.root,
            wait_seconds=1,
            poll_seconds=0.01,
            min_interval_seconds=0,
        )
        first.__enter__()
        release = threading.Timer(0.05, lambda: first.__exit__(None, None, None))
        release.start()
        try:
            with RemoteActionLock(
                self.root,
                wait_seconds=1,
                poll_seconds=0.01,
                min_interval_seconds=0,
            ) as second:
                self.assertTrue(second.acquired)
        finally:
            release.join()

    def test_remote_lock_honors_registered_backoff(self) -> None:
        with RemoteActionLock(self.root, min_interval_seconds=0) as first:
            first.register_backoff(0.05)
        started = time.monotonic()
        with RemoteActionLock(self.root, min_interval_seconds=0):
            pass
        self.assertGreaterEqual(time.monotonic() - started, 0.04)

    def test_remote_lock_uses_exponential_429_backoff_and_can_reset(self) -> None:
        with RemoteActionLock(self.root, min_interval_seconds=0) as lock:
            first = lock.register_backoff(1, max_seconds=10)
            second = lock.register_backoff(1, max_seconds=10)
            third = lock.register_backoff(1, max_seconds=3)
            state = json.loads(lock.backoff_path.read_text(encoding="utf-8"))
            lock.clear_backoff()

        self.assertEqual((first, second, third), (1, 2, 3))
        self.assertEqual(state["consecutive429"], 3)
        self.assertEqual(state["delaySeconds"], 3)
        self.assertFalse(lock.backoff_path.exists())

    def test_remote_lock_retries_transient_windows_release_error(self) -> None:
        lock = RemoteActionLock(self.root, poll_seconds=0.001, min_interval_seconds=0)
        lock.__enter__()
        original_unlink = Path.unlink
        attempts = 0

        def flaky_unlink(path: Path, *args: object, **kwargs: object) -> None:
            nonlocal attempts
            if path == lock.path and attempts == 0:
                attempts += 1
                raise PermissionError("simulated Windows sharing violation")
            original_unlink(path, *args, **kwargs)

        with patch.object(Path, "unlink", new=flaky_unlink):
            lock.__exit__(None, None, None)

        self.assertEqual(attempts, 1)
        self.assertFalse(lock.path.exists())


if __name__ == "__main__":
    unittest.main()
