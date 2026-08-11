# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        mod, n = 1_000_000_007, len(grid[0])
        dp = [[0] * 16 for _ in range(n)]
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                current = [0] * 16
                if i == 0 and j == 0:
                    current[value] = 1
                else:
                    if i:
                        for x, count in enumerate(dp[j]):
                            current[x ^ value] += count
                    if j:
                        for x, count in enumerate(dp[j - 1]):
                            current[x ^ value] += count
                    current = [count % mod for count in current]
                dp[j] = current
        return dp[-1][k]
