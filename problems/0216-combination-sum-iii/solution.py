# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:33:28Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, remaining: int, path: List[int]) -> None:
            if len(path) == k:
                if remaining == 0:
                    result.append(path[:])
                return
            for value in range(start, 10):
                if value > remaining:
                    break
                path.append(value)
                backtrack(value + 1, remaining - value, path)
                path.pop()

        backtrack(1, n, [])
        return result
