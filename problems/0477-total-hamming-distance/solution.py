# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:10:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        for bit in range(30):
            ones = sum((number >> bit) & 1 for number in nums)
            total += ones * (len(nums) - ones)
        return total
