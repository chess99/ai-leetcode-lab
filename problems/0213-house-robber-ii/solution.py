# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:33:28Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def linear(houses: List[int]) -> int:
            previous, current = 0, 0
            for money in houses:
                previous, current = current, max(current, previous + money)
            return current

        return max(linear(nums[:-1]), linear(nums[1:]))
