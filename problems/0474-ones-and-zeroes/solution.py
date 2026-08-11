# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:08:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for string in strs:
            zeros = string.count("0")
            ones = len(string) - zeros
            for zero_limit in range(m, zeros - 1, -1):
                for one_limit in range(n, ones - 1, -1):
                    dp[zero_limit][one_limit] = max(
                        dp[zero_limit][one_limit],
                        dp[zero_limit - zeros][one_limit - ones] + 1,
                    )
        return dp[m][n]
