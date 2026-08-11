# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:11Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = nums.count(1)
        if ones: return len(nums) - ones
        best = len(nums) + 1
        for i in range(len(nums)):
            g = 0
            for j in range(i, len(nums)):
                g = gcd(g, nums[j])
                if g == 1: best = min(best, j - i + 1); break
        return -1 if best == len(nums) + 1 else len(nums) + best - 2
