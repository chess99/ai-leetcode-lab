# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:16:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(start: int) -> None:
            if len(path) == k:
                result.append(path[:])
                return
            needed = k - len(path)
            for value in range(start, n - needed + 2):
                path.append(value)
                backtrack(value + 1)
                path.pop()

        backtrack(1)
        return result
