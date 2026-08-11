# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        window_size = 2 * k + 1
        averages = [-1] * length

        if window_size > length:
            return averages

        window_sum = sum(nums[:window_size])
        averages[k] = window_sum // window_size

        for right in range(window_size, length):
            window_sum += nums[right] - nums[right - window_size]
            averages[right - k] = window_sum // window_size

        return averages
