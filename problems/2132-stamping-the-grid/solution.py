# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        rows = len(grid)
        columns = len(grid[0])
        prefix = [[0] * (columns + 1) for _ in range(rows + 1)]
        for row in range(rows):
            running = 0
            for column in range(columns):
                running += grid[row][column]
                prefix[row + 1][column + 1] = prefix[row][column + 1] + running

        difference = [[0] * (columns + 1) for _ in range(rows + 1)]
        for row in range(rows - stampHeight + 1):
            bottom = row + stampHeight
            for column in range(columns - stampWidth + 1):
                right = column + stampWidth
                occupied = (prefix[bottom][right] - prefix[row][right]
                            - prefix[bottom][column] + prefix[row][column])
                if occupied == 0:
                    difference[row][column] += 1
                    difference[bottom][column] -= 1
                    difference[row][right] -= 1
                    difference[bottom][right] += 1

        for row in range(rows):
            for column in range(columns):
                if row:
                    difference[row][column] += difference[row - 1][column]
                if column:
                    difference[row][column] += difference[row][column - 1]
                if row and column:
                    difference[row][column] -= difference[row - 1][column - 1]
                if grid[row][column] == 0 and difference[row][column] == 0:
                    return False
        return True
