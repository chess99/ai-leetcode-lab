# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:24:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = 0
        end = -1
        maximum = float("-inf")
        minimum = float("inf")
        for index, number in enumerate(nums):
            maximum = max(maximum, number)
            if number < maximum:
                end = index

        for index in range(len(nums) - 1, -1, -1):
            minimum = min(minimum, nums[index])
            if nums[index] > minimum:
                start = index
        return end - start + 1
