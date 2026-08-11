# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:53:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        longest = 0

        for right, value in enumerate(nums):
            if value == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            longest = max(longest, right - left)

        return longest
