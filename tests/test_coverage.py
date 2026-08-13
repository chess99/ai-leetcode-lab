from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from ai_leetcode.coverage import audit_coverage


class CoverageTests(unittest.TestCase):
    def test_audit_separates_real_candidate_from_placeholder(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "archive").mkdir()
            (root / "archive" / "catalog.json").write_text(
                json.dumps(
                    {
                        "problems": [
                            {"titleSlug": "ok", "paidOnly": False},
                            {"titleSlug": "todo", "paidOnly": False},
                            {"titleSlug": "paid", "paidOnly": True},
                        ]
                    }
                ),
                encoding="utf-8",
            )
            problem_root = root / "problems"
            for slug, source in (
                ("ok", "class Solution:\n    pass\n"),
                ("todo", "raise NotImplementedError()\n"),
            ):
                target = problem_root / slug
                target.mkdir(parents=True)
                (target / "meta.json").write_text(
                    json.dumps(
                        {
                            "titleSlug": slug,
                            "language": "python3",
                            "solutionFile": "solution.py",
                        }
                    ),
                    encoding="utf-8",
                )
                (target / "problem.md").write_text("problem", encoding="utf-8")
                (target / "approach.md").write_text("approach", encoding="utf-8")
                (target / "solution.py").write_text(source, encoding="utf-8")

            report = audit_coverage(root=root)
            self.assertEqual(report["eligibleProblems"], 2)
            self.assertEqual(report["directoriesPresent"], 2)
            self.assertEqual(report["validLocalCandidates"], 1)
            self.assertEqual(report["placeholderSlugs"], ["todo"])
            self.assertEqual(len(report["candidateCodeSha256"]["ok"]), 64)
            self.assertIn("javascript", report["syntaxGateAvailability"])

    def test_audit_detects_missing_directory_and_language_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "archive").mkdir()
            (root / "archive" / "catalog.json").write_text(
                json.dumps(
                    {
                        "problems": [
                            {"titleSlug": "missing", "paidOnly": False},
                            {"titleSlug": "wrong", "paidOnly": False},
                        ]
                    }
                ),
                encoding="utf-8",
            )
            target = root / "problems" / "wrong"
            target.mkdir(parents=True)
            (target / "meta.json").write_text(
                json.dumps(
                    {
                        "titleSlug": "wrong",
                        "language": "javascript",
                        "solutionFile": "solution.py",
                    }
                ),
                encoding="utf-8",
            )
            for name in ("problem.md", "approach.md", "solution.py"):
                (target / name).write_text("x", encoding="utf-8")

            report = audit_coverage(root=root)
            self.assertEqual(report["missingDirectories"], ["missing"])
            self.assertEqual(report["validLocalCandidates"], 0)
            self.assertTrue(
                any(issue["kind"] == "language_extension_mismatch" for issue in report["issues"])
            )


if __name__ == "__main__":
    unittest.main()
