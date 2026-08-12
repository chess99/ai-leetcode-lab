# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        longest = 0
        for right, value in enumerate(nums):
            while value > nums[left] * k:
                left += 1
            longest = max(longest, right - left + 1)
        return len(nums) - longest
