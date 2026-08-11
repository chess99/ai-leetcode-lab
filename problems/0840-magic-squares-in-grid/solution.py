# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:48:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])

        def is_magic(row: int, column: int) -> bool:
            values = [grid[row + offset_row][column + offset_column]
                      for offset_row in range(3) for offset_column in range(3)]
            if set(values) != set(range(1, 10)):
                return False
            return (all(sum(grid[row + offset_row][column:column + 3]) == 15
                        for offset_row in range(3))
                    and all(sum(grid[row + offset_row][column + offset_column]
                                for offset_row in range(3)) == 15
                            for offset_column in range(3))
                    and grid[row][column] + grid[row + 1][column + 1] + grid[row + 2][column + 2] == 15
                    and grid[row][column + 2] + grid[row + 1][column + 1] + grid[row + 2][column] == 15)

        return sum(is_magic(row, column)
                   for row in range(rows - 2) for column in range(columns - 2))
