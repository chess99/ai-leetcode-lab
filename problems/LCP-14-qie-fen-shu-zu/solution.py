# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:44Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        maximum = max(nums)
        spf = list(range(maximum + 1))
        for value in range(2, int(maximum ** 0.5) + 1):
            if spf[value] != value:
                continue
            for multiple in range(value * value, maximum + 1, value):
                if spf[multiple] == multiple:
                    spf[multiple] = value

        def factors(value):
            result = []
            while value > 1:
                prime = spf[value]
                result.append(prime)
                while value % prime == 0:
                    value //= prime
            return result

        infinity = len(nums) + 1
        best = [infinity] * (maximum + 1)
        dp = [0] * len(nums)
        for index, value in enumerate(nums):
            primes = factors(value)
            previous = 0 if index == 0 else dp[index - 1]
            for prime in primes:
                best[prime] = min(best[prime], previous)
            dp[index] = 1 + min(best[prime] for prime in primes)
        return dp[-1]
