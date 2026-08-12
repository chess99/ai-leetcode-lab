# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:23Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd
from typing import List


class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        size = 1 << len(target)
        lcm = [1] * size
        for mask in range(1, size):
            bit = mask & -mask
            index = bit.bit_length() - 1
            previous = lcm[mask ^ bit]
            lcm[mask] = previous // gcd(previous, target[index]) * target[index]

        inf = 10**30
        dp = [inf] * size
        dp[0] = 0
        for value in nums:
            new = dp[:]
            for covered in range(size):
                if dp[covered] == inf:
                    continue
                for chosen in range(1, size):
                    increment = (-value) % lcm[chosen]
                    combined = covered | chosen
                    new[combined] = min(new[combined], dp[covered] + increment)
            dp = new
        return dp[-1]
