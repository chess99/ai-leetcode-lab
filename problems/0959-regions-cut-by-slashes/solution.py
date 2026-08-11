# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:01:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        size = len(grid) * 3
        expanded = [[0] * size for _ in range(size)]
        for row, line in enumerate(grid):
            for column, character in enumerate(line):
                if character == "/":
                    expanded[row * 3][column * 3 + 2] = 1
                    expanded[row * 3 + 1][column * 3 + 1] = 1
                    expanded[row * 3 + 2][column * 3] = 1
                elif character == "\\":
                    expanded[row * 3][column * 3] = 1
                    expanded[row * 3 + 1][column * 3 + 1] = 1
                    expanded[row * 3 + 2][column * 3 + 2] = 1

        regions = 0
        for row in range(size):
            for column in range(size):
                if expanded[row][column]:
                    continue
                regions += 1
                expanded[row][column] = 1
                stack = [(row, column)]
                while stack:
                    current_row, current_column = stack.pop()
                    for next_row, next_column in ((current_row - 1, current_column),
                                                  (current_row + 1, current_column),
                                                  (current_row, current_column - 1),
                                                  (current_row, current_column + 1)):
                        if 0 <= next_row < size and 0 <= next_column < size and not expanded[next_row][next_column]:
                            expanded[next_row][next_column] = 1
                            stack.append((next_row, next_column))
        return regions
