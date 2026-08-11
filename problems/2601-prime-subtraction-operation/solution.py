# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:27Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        limit = max(nums)
        is_prime = [True] * (limit + 1)
        is_prime[0] = False
        if limit >= 1:
            is_prime[1] = False
        primes = []
        for value in range(2, limit + 1):
            if is_prime[value]:
                primes.append(value)
                for multiple in range(value * value, limit + 1, value):
                    is_prime[multiple] = False

        previous = 0
        for value in nums:
            index = bisect_left(primes, value - previous) - 1
            current = value - (primes[index] if index >= 0 else 0)
            if current <= previous:
                return False
            previous = current
        return True
