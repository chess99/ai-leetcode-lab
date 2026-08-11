# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:43:09Z
# Experiment: ai-leetcode-lab, round 1
from math import isqrt
from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divisor_sum(value: int) -> int:
            if value == 1:
                return 0
            count, total = 2, value + 1
            for divisor in range(2, isqrt(value) + 1):
                if value % divisor == 0:
                    paired = value // divisor
                    if divisor == paired:
                        count += 1
                        total += divisor
                    else:
                        count += 2
                        total += divisor + paired
                    if count > 4:
                        return 0
            return total if count == 4 else 0

        return sum(divisor_sum(value) for value in nums)
