from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from ai_leetcode.coverage import audit_coverage


class CoverageTests(unittest.TestCase):
    @staticmethod
    def _write_python_archive(root: Path, directory_name: str, template: str) -> None:
        archive_root = root / "archive" / "problems"
        archive_root.mkdir(parents=True, exist_ok=True)
        (archive_root / f"{directory_name}.json").write_text(
            json.dumps(
                {
                    "question": {
                        "codeSnippets": [
                            {"langSlug": "python3", "code": template}
                        ]
                    }
                }
            ),
            encoding="utf-8",
        )

    def _audit_single_python(self, template: str, candidate: str) -> dict:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        (root / "archive").mkdir()
        (root / "archive" / "catalog.json").write_text(
            json.dumps({"problems": [{"titleSlug": "sample", "paidOnly": False}]}),
            encoding="utf-8",
        )
        target = root / "problems" / "sample"
        target.mkdir(parents=True)
        (target / "meta.json").write_text(
            json.dumps(
                {
                    "titleSlug": "sample",
                    "language": "python3",
                    "solutionFile": "solution.py",
                }
            ),
            encoding="utf-8",
        )
        for name, content in (
            ("problem.md", "problem"),
            ("approach.md", "approach"),
            ("solution.py", candidate),
        ):
            (target / name).write_text(content, encoding="utf-8")
        self._write_python_archive(root, "sample", template)
        return audit_coverage(root=root)

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

    def test_python_interface_detects_class_mismatch(self) -> None:
        report = self._audit_single_python(
            "class Expected:\n    def run(self, value: int):\n        ",
            "class Wrong:\n    def run(self, value):\n        return value\n",
        )
        self.assertEqual(report["validLocalCandidates"], 0)
        self.assertEqual(report["issues"][0]["kind"], "python_interface_class_mismatch")

    def test_python_interface_detects_missing_method(self) -> None:
        report = self._audit_single_python(
            "class Solution:\n    def run(self, value: int):\n        ",
            "class Solution:\n    pass\n",
        )
        self.assertEqual(report["issues"][0]["kind"], "python_interface_methods_missing")

    def test_python_interface_detects_incompatible_argument_count(self) -> None:
        report = self._audit_single_python(
            "class Solution:\n    def run(self, left: int, right: int):\n        ",
            "class Solution:\n    def run(self, value):\n        return value\n",
        )
        self.assertEqual(report["issues"][0]["kind"], "python_interface_arity_mismatch")

    def test_python_interface_parses_multiline_empty_template(self) -> None:
        report = self._audit_single_python(
            "class Solution:\n"
            "    def run(\n"
            "        self,\n"
            "        left: int,\n"
            "        right: int,\n"
            "    ) -> int:\n"
            "        ",
            "class Solution:\n"
            "    def run(self, first, second=0):\n"
            "        return first + second\n",
        )
        self.assertEqual(report["validLocalCandidates"], 1)
        self.assertEqual(report["interfaceChecked"], {"python3": 1})
        self.assertEqual(report["issues"], [])

    def test_python_future_annotations_is_submission_incompatible(self) -> None:
        report = self._audit_single_python(
            "class Solution:\n    def run(self, value: int):\n        ",
            "from __future__ import annotations\n"
            "class Solution:\n"
            "    def run(self, value):\n"
            "        return value\n",
        )
        self.assertEqual(report["validLocalCandidates"], 0)
        self.assertEqual(
            report["issues"][0]["kind"],
            "python_submission_incompatible_future_annotations",
        )


if __name__ == "__main__":
    unittest.main()
