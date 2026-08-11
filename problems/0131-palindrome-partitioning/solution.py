# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:24:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(start: int, parts: List[str]) -> None:
            if start == len(s):
                result.append(parts[:])
                return
            for end in range(start + 1, len(s) + 1):
                part = s[start:end]
                if part == part[::-1]:
                    parts.append(part)
                    backtrack(end, parts)
                    parts.pop()

        backtrack(0, [])
        return result
