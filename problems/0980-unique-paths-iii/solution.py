# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:05Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        remaining = 0
        start = None
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] != -1:
                    remaining += 1
                if grid[row][column] == 1:
                    start = (row, column)

        def search(row, column, left):
            if grid[row][column] == 2:
                return int(left == 1)
            original = grid[row][column]
            grid[row][column] = -1
            answer = 0
            for next_row, next_column in ((row-1,column),(row+1,column),
                                          (row,column-1),(row,column+1)):
                if (0 <= next_row < rows and 0 <= next_column < columns and
                        grid[next_row][next_column] != -1):
                    answer += search(next_row, next_column, left - 1)
            grid[row][column] = original
            return answer

        return search(start[0], start[1], remaining)
