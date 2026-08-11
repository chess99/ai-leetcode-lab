# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows, columns = len(grid), len(grid[0])
        largest = set()

        def record(value: int) -> None:
            largest.add(value)
            if len(largest) > 3:
                largest.remove(min(largest))

        for row in range(rows):
            for column in range(columns):
                record(grid[row][column])
                max_radius = min(row, column, rows - 1 - row, columns - 1 - column)
                for radius in range(1, max_radius + 1):
                    perimeter = 0
                    for offset in range(radius):
                        perimeter += grid[row - radius + offset][column + offset]
                        perimeter += grid[row + offset][column + radius - offset]
                        perimeter += grid[row + radius - offset][column - offset]
                        perimeter += grid[row - offset][column - radius + offset]
                    record(perimeter)

        return sorted(largest, reverse=True)
