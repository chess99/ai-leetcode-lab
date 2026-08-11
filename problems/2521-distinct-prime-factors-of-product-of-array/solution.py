# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:25Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors = set()
        for value in nums:
            d = 2
            while d * d <= value:
                if value % d == 0:
                    factors.add(d)
                    while value % d == 0:
                        value //= d
                d += 1
            if value > 1:
                factors.add(value)
        return len(factors)
