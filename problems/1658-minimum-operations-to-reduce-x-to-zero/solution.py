# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:28Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0: return -1
        left = total = 0; longest = -1
        for right, value in enumerate(nums):
            total += value
            while total > target: total -= nums[left]; left += 1
            if total == target: longest = max(longest, right - left + 1)
        return -1 if longest < 0 else len(nums) - longest
