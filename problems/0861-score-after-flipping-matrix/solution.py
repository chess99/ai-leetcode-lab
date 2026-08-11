# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:53:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        score = rows * (1 << (columns - 1))
        for column in range(1, columns):
            ones = sum(grid[row][column] == grid[row][0] for row in range(rows))
            score += max(ones, rows - ones) * (1 << (columns - column - 1))
        return score
