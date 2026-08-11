# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:14:59Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        maximum = [[0] * columns for _ in range(rows)]
        minimum = [[0] * columns for _ in range(rows)]
        maximum[0][0] = minimum[0][0] = grid[0][0]

        for row in range(rows):
            for column in range(columns):
                if row == 0 and column == 0:
                    continue

                candidates = []
                if row > 0:
                    candidates.extend((maximum[row - 1][column], minimum[row - 1][column]))
                if column > 0:
                    candidates.extend((maximum[row][column - 1], minimum[row][column - 1]))

                products = [value * grid[row][column] for value in candidates]
                maximum[row][column] = max(products)
                minimum[row][column] = min(products)

        answer = maximum[-1][-1]
        return answer % 1_000_000_007 if answer >= 0 else -1
