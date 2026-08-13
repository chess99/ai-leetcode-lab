# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-13T00:00:00Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countArrays(self, digitSum: List[int]) -> int:
        tovanelqir = digitSum
        mod = 1_000_000_007
        limit = 5000
        sums = [sum(map(int, str(value))) for value in range(limit + 1)]

        dp = [int(sums[value] == tovanelqir[0]) for value in range(limit + 1)]
        for target in tovanelqir[1:]:
            prefix = 0
            next_dp = [0] * (limit + 1)
            for value in range(limit + 1):
                prefix = (prefix + dp[value]) % mod
                if sums[value] == target:
                    next_dp[value] = prefix
            dp = next_dp
        return sum(dp) % mod
