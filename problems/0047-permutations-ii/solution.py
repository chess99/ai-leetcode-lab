# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:12:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        used = [False] * len(nums)

        def backtrack(path: List[int]) -> None:
            if len(path) == len(nums):
                result.append(path[:])
                return
            for index, value in enumerate(nums):
                if used[index] or (index > 0 and value == nums[index - 1] and not used[index - 1]):
                    continue
                used[index] = True
                path.append(value)
                backtrack(path)
                path.pop()
                used[index] = False

        backtrack([])
        return result
