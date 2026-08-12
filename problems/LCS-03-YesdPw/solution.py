# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def largestArea(self, grid: List[str]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = [[False] * columns for _ in range(rows)]
        answer = 0
        for start_row in range(rows):
            for start_column in range(columns):
                if visited[start_row][start_column] or grid[start_row][start_column] == '0':
                    continue
                theme = grid[start_row][start_column]
                visited[start_row][start_column] = True
                stack = [(start_row, start_column)]
                area = 0
                enclosed = True
                while stack:
                    row, column = stack.pop()
                    area += 1
                    for next_row, next_column in ((row - 1, column), (row + 1, column),
                                                  (row, column - 1), (row, column + 1)):
                        if not (0 <= next_row < rows and 0 <= next_column < columns):
                            enclosed = False
                        elif grid[next_row][next_column] == '0':
                            enclosed = False
                        elif (grid[next_row][next_column] == theme
                              and not visited[next_row][next_column]):
                            visited[next_row][next_column] = True
                            stack.append((next_row, next_column))
                if enclosed:
                    answer = max(answer, area)
        return answer
