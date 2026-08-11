# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:25Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        dp = grid[0][:]
        columns = len(grid[0])

        for row in range(len(grid) - 1):
            next_dp = [float("inf")] * columns
            for source_column, value in enumerate(grid[row]):
                for target_column in range(columns):
                    next_dp[target_column] = min(
                        next_dp[target_column],
                        dp[source_column] + moveCost[value][target_column] + grid[row + 1][target_column],
                    )
            dp = next_dp

        return min(dp)
