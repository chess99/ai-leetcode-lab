# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:22Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        ways = 0

        for value in nums[:-1]:
            left_sum += value
            right_sum -= value
            if left_sum >= right_sum:
                ways += 1

        return ways
