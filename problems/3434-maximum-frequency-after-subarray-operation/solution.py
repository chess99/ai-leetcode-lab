# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        base = nums.count(k)
        best = 0
        for value in set(nums):
            if value == k:
                continue
            current = 0
            for number in nums:
                current = max(0, current + (1 if number == value else -1 if number == k else 0))
                best = max(best, current)
        return base + best
