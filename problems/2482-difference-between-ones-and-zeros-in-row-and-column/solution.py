# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:22Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        row_ones = [sum(row) for row in grid]
        col_ones = [sum(grid[row][col] for row in range(rows)) for col in range(cols)]

        return [
            [2 * row_ones[row] + 2 * col_ones[col] - rows - cols for col in range(cols)]
            for row in range(rows)
        ]
