from __future__ import annotations

import unittest

from ai_leetcode.cli import _candidate_profile


class CandidateProfileTests(unittest.TestCase):
    def test_latest_revision_overrides_original_profile(self) -> None:
        source = """# Profile: terra-medium
# Revised by: Codex Desktop / gpt-5.6-sol / medium / sol-medium
# Revised by: Codex Desktop / gpt-5.6-sol / high / sol-high
class Solution:
    pass
"""
        self.assertEqual(_candidate_profile(source), "sol-high")

    def test_original_profile_is_used_without_revision(self) -> None:
        self.assertEqual(
            _candidate_profile("# Profile: terra-medium\nclass Solution:\n    pass\n"),
            "terra-medium",
        )


if __name__ == "__main__":
    unittest.main()
