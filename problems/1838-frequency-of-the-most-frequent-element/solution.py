# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:34Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        window_sum = 0
        best = 0

        for right, value in enumerate(nums):
            window_sum += value
            while value * (right - left + 1) - window_sum > k:
                window_sum -= nums[left]
                left += 1
            best = max(best, right - left + 1)

        return best
