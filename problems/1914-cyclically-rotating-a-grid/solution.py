# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:04Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, columns = len(grid), len(grid[0])

        for layer in range(min(rows, columns) // 2):
            top, left = layer, layer
            bottom, right = rows - 1 - layer, columns - 1 - layer
            positions = []

            for column in range(left, right + 1):
                positions.append((top, column))
            for row in range(top + 1, bottom + 1):
                positions.append((row, right))
            for column in range(right - 1, left - 1, -1):
                positions.append((bottom, column))
            for row in range(bottom - 1, top, -1):
                positions.append((row, left))

            values = [grid[row][column] for row, column in positions]
            shift = k % len(positions)
            for index, (row, column) in enumerate(positions):
                grid[row][column] = values[(index + shift) % len(positions)]

        return grid
