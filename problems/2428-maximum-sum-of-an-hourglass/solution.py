# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maximum = 0

        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                hourglass = (
                    grid[row][col]
                    + grid[row][col + 1]
                    + grid[row][col + 2]
                    + grid[row + 1][col + 1]
                    + grid[row + 2][col]
                    + grid[row + 2][col + 1]
                    + grid[row + 2][col + 2]
                )
                maximum = max(maximum, hourglass)

        return maximum
