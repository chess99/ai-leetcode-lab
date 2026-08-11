# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:26Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        modulo = 1_000_000_007
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        masks = {}
        for value in range(2, 31):
            mask = 0
            valid = True
            for bit, prime in enumerate(primes):
                if value % (prime * prime) == 0:
                    valid = False
                    break
                if value % prime == 0:
                    mask |= 1 << bit
            if valid:
                masks[value] = mask
        counts = Counter(nums)
        dp = [0] * (1 << len(primes))
        dp[0] = pow(2, counts[1], modulo)
        for value, mask in masks.items():
            if counts[value]:
                for used in range(len(dp) - 1, -1, -1):
                    if used & mask == 0:
                        dp[used | mask] = (dp[used | mask] + dp[used] * counts[value]) % modulo
        return (sum(dp) - 1) % modulo
