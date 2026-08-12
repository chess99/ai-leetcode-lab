# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:55Z
# Experiment: ai-leetcode-lab, round 1
from math import comb


class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        zanoprelix = (n, k)
        length = k
        while True:
            amount = comb(length - 1, k - 1)
            if n <= amount:
                break
            n -= amount
            length += 1

        remaining_ones = k - 1
        answer = 1 << (length - 1)
        for bit in range(length - 2, -1, -1):
            zero_count = comb(bit, remaining_ones) if remaining_ones <= bit else 0
            if n > zero_count:
                n -= zero_count
                answer |= 1 << bit
                remaining_ones -= 1
        return answer
