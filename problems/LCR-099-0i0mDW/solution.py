# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        columns = len(grid[0])
        dp = [float('inf')] * columns
        dp[0] = 0
        for row in grid:
            dp[0] += row[0]
            for column in range(1, columns):
                dp[column] = min(dp[column], dp[column - 1]) + row[column]
        return dp[-1]
