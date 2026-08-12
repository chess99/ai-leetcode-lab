# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        answer = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 0:
                    continue
                grid[row][column] = 0
                stack = [(row, column)]
                area = 0
                while stack:
                    current_row, current_column = stack.pop()
                    area += 1
                    for next_row, next_column in ((current_row - 1, current_column),
                                                  (current_row + 1, current_column),
                                                  (current_row, current_column - 1),
                                                  (current_row, current_column + 1)):
                        if (0 <= next_row < rows and 0 <= next_column < columns
                                and grid[next_row][next_column] == 1):
                            grid[next_row][next_column] = 0
                            stack.append((next_row, next_column))
                answer = max(answer, area)
        return answer
