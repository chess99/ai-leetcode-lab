# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        canovireth = (grid, limit)
        columns = len(grid[0])
        dp = [1] * columns
        for right in range(columns):
            for left in range(right):
                if all(abs(row[right] - row[left]) <= limit for row in grid):
                    dp[right] = max(dp[right], dp[left] + 1)
        return max(dp)
