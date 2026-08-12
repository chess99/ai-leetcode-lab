# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = total = 0
        answer = len(nums) + 1
        for right, value in enumerate(nums):
            total += value
            while total >= target:
                answer = min(answer, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if answer > len(nums) else answer
