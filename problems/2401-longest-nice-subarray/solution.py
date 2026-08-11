# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        used_bits = 0
        left = 0
        longest = 0

        for right, number in enumerate(nums):
            while used_bits & number:
                used_bits ^= nums[left]
                left += 1

            used_bits |= number
            longest = max(longest, right - left + 1)

        return longest
