# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:41:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        score = nums[0] + nums[1]
        operations = 1

        for index in range(2, len(nums) - 1, 2):
            if nums[index] + nums[index + 1] != score:
                break
            operations += 1

        return operations
