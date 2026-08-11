# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                enter = (i + 1) * (j + 1)
                best = float('inf')
                if i:
                    wait = 0 if i == 1 and j == 0 else waitCost[i - 1][j]
                    best = min(best, dp[i - 1][j] + wait)
                if j:
                    wait = 0 if i == 0 and j == 1 else waitCost[i][j - 1]
                    best = min(best, dp[i][j - 1] + wait)
                dp[i][j] = best + enter
        return dp[-1][-1]
