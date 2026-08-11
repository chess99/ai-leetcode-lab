# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:27Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        if ones <= 1:
            return 0

        circular = nums + nums
        current_ones = sum(circular[:ones])
        maximum_ones = current_ones
        for right in range(ones, len(circular)):
            current_ones += circular[right] - circular[right - ones]
            maximum_ones = max(maximum_ones, current_ones)

        return ones - maximum_ones
