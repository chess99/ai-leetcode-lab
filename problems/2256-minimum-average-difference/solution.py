# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:20Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        best_difference = float("inf")
        best_index = 0

        for index, value in enumerate(nums):
            left_sum += value
            left_average = left_sum // (index + 1)
            right_count = len(nums) - index - 1
            right_average = (total - left_sum) // right_count if right_count else 0
            difference = abs(left_average - right_average)
            if difference < best_difference:
                best_difference = difference
                best_index = index

        return best_index
