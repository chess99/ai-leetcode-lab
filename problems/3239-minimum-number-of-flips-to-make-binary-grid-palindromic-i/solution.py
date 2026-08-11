# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_cost = sum(grid[row][col] != grid[row][cols - 1 - col] for row in range(rows) for col in range(cols // 2))
        col_cost = sum(grid[row][col] != grid[rows - 1 - row][col] for row in range(rows // 2) for col in range(cols))
        return min(row_cost, col_cost)
