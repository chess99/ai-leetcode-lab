# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        modulo = 10**9 + 7
        exponent_prefix = [0]
        bit = 0

        while n > 0:
            if n & 1:
                exponent_prefix.append(exponent_prefix[-1] + bit)
            n >>= 1
            bit += 1

        return [
            pow(
                2,
                exponent_prefix[right + 1] - exponent_prefix[left],
                modulo,
            )
            for left, right in queries
        ]
