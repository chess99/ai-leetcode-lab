from __future__ import annotations

import unittest

from ai_leetcode.security import scan_added_lines


class SecurityTests(unittest.TestCase):
    def test_detects_leetcode_session(self) -> None:
        findings = scan_added_lines(["+LEETCODE_SESSION=" + "x" * 40])
        self.assertTrue(findings)

    def test_allows_empty_example(self) -> None:
        self.assertEqual(scan_added_lines(["+LEETCODE_SESSION=", "+LEETCODE_CSRF_TOKEN="]), [])

    def test_ignores_removed_secret(self) -> None:
        self.assertEqual(scan_added_lines(["-LEETCODE_SESSION=" + "x" * 40]), [])


if __name__ == "__main__":
    unittest.main()
