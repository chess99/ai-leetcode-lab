# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        from math import isqrt

        limit = isqrt(r)
        prime = [True] * (limit + 1)
        if limit >= 0:
            prime[0] = False
        if limit >= 1:
            prime[1] = False
        for value in range(2, isqrt(limit) + 1):
            if prime[value]:
                prime[value * value:limit + 1:value] = [False] * (((limit - value * value) // value) + 1)
        special = sum(prime[value] and l <= value * value <= r for value in range(2, limit + 1))
        return r - l + 1 - special
