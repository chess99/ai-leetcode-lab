# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:11:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrack(start: int) -> None:
            if len(path) >= 2:
                result.append(path.copy())

            used = set()
            for index in range(start, len(nums)):
                value = nums[index]
                if value in used or (path and value < path[-1]):
                    continue
                used.add(value)
                path.append(value)
                backtrack(index + 1)
                path.pop()

        backtrack(0)
        return result
