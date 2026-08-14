# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Created: 2026-08-14
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        operations = 0
        lower_levels = 0

        for index in range(1, len(nums)):
            if nums[index] != nums[index - 1]:
                lower_levels += 1
            operations += lower_levels

        return operations
