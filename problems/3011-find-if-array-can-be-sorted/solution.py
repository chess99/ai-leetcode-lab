# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        previous_max = 0
        index = 0
        while index < len(nums):
            bits = nums[index].bit_count()
            current_min = current_max = nums[index]
            index += 1
            while index < len(nums) and nums[index].bit_count() == bits:
                current_min = min(current_min, nums[index])
                current_max = max(current_max, nums[index])
                index += 1
            if current_min < previous_max:
                return False
            previous_max = current_max
        return True
