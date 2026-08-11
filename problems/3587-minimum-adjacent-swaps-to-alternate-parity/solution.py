# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        odd = [i for i, value in enumerate(nums) if value & 1]
        even = len(nums) - len(odd)
        if abs(len(odd) - even) > 1: return -1
        def cost(odd_first: bool) -> int:
            return sum(abs(pos - (2 * i + (0 if odd_first else 1))) for i, pos in enumerate(odd))
        if len(odd) > even: return cost(True)
        if even > len(odd): return cost(False)
        return min(cost(True), cost(False))
