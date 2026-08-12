# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        pairs = sorted(zip(nums, cost))
        total_weight = sum(cost)
        accumulated = 0
        median = pairs[0][0]
        for value, weight in pairs:
            accumulated += weight
            if accumulated * 2 >= total_weight:
                median = value
                break
        return sum(abs(value - median) * weight for value, weight in pairs)
