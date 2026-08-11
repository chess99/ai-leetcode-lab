# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:32:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = len(nums) + 1
        left = total = 0
        for right, value in enumerate(nums):
            total += value
            while total >= target:
                best = min(best, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if best == len(nums) + 1 else best
