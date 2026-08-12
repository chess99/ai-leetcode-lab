# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0]); dp = [float("inf")] * (n + 1); dp[n - 1] = 1
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1): dp[col] = max(1, min(dp[col], dp[col + 1]) - dungeon[row][col])
        return dp[0]
