# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:37:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = [sum(row) for row in grid]
        cols = [sum(grid[row][col] for row in range(len(grid))) for col in range(len(grid[0]))]
        return sum(value and (rows[row] > 1 or cols[col] > 1) for row, line in enumerate(grid) for col, value in enumerate(line))
