# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:17:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []

        def backtrack(start: int, subset: List[int]) -> None:
            subsets.append(subset.copy())
            for index in range(start, len(nums)):
                if index > start and nums[index] == nums[index - 1]:
                    continue
                subset.append(nums[index])
                backtrack(index + 1, subset)
                subset.pop()

        backtrack(0, [])
        return subsets
