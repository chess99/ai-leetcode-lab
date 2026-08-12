# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def backtrack(first: int) -> None:
            if first == len(nums):
                answer.append(nums[:])
                return
            for index in range(first, len(nums)):
                nums[first], nums[index] = nums[index], nums[first]
                backtrack(first + 1)
                nums[first], nums[index] = nums[index], nums[first]

        backtrack(0)
        return answer
