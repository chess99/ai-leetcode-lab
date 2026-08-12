# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        mod = 1_000_000_007
        required = {end: count for end, count in requirements}
        limit = max(required.values())
        dp = [1] + [0] * limit

        for length in range(1, n + 1):
            new = [0] * (limit + 1)
            window = 0
            for inversions in range(limit + 1):
                window += dp[inversions]
                if inversions >= length:
                    window -= dp[inversions - length]
                new[inversions] = window % mod

            need = required.get(length - 1)
            if need is not None:
                if need > length * (length - 1) // 2:
                    return 0
                ways = new[need]
                new = [0] * (limit + 1)
                new[need] = ways
            dp = new

        return dp[required[n - 1]]
