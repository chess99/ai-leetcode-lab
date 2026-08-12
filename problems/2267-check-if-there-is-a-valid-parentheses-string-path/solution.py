# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:45Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        columns = len(grid[0])
        path_length = rows + columns - 1
        if (path_length % 2 or grid[0][0] == ")"
                or grid[-1][-1] == "("):
            return False

        previous = [set() for _ in range(columns)]
        for row in range(rows):
            current = [set() for _ in range(columns)]
            for column in range(columns):
                source = set()
                if row == 0 and column == 0:
                    source.add(0)
                if row:
                    source.update(previous[column])
                if column:
                    source.update(current[column - 1])
                change = 1 if grid[row][column] == "(" else -1
                remaining = (rows - 1 - row) + (columns - 1 - column)
                current[column] = {
                    balance + change for balance in source
                    if 0 <= balance + change <= remaining
                }
            previous = current
        return 0 in previous[-1]
