# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        row_twos = [[0] * (cols + 1) for _ in range(rows)]
        row_fives = [[0] * (cols + 1) for _ in range(rows)]
        col_twos = [[0] * cols for _ in range(rows + 1)]
        col_fives = [[0] * cols for _ in range(rows + 1)]

        for row in range(rows):
            for col in range(cols):
                value = grid[row][col]
                twos = 0
                fives = 0

                while value % 2 == 0:
                    twos += 1
                    value //= 2
                while value % 5 == 0:
                    fives += 1
                    value //= 5

                row_twos[row][col + 1] = row_twos[row][col] + twos
                row_fives[row][col + 1] = row_fives[row][col] + fives
                col_twos[row + 1][col] = col_twos[row][col] + twos
                col_fives[row + 1][col] = col_fives[row][col] + fives

        answer = 0

        for row in range(rows):
            for col in range(cols):
                cell_twos = row_twos[row][col + 1] - row_twos[row][col]
                cell_fives = row_fives[row][col + 1] - row_fives[row][col]

                left = (
                    row_twos[row][col + 1],
                    row_fives[row][col + 1],
                )
                right = (
                    row_twos[row][cols] - row_twos[row][col],
                    row_fives[row][cols] - row_fives[row][col],
                )
                up = (
                    col_twos[row + 1][col],
                    col_fives[row + 1][col],
                )
                down = (
                    col_twos[rows][col] - col_twos[row][col],
                    col_fives[rows][col] - col_fives[row][col],
                )

                for horizontal in (left, right):
                    for vertical in (up, down):
                        total_twos = horizontal[0] + vertical[0] - cell_twos
                        total_fives = horizontal[1] + vertical[1] - cell_fives
                        answer = max(answer, min(total_twos, total_fives))

        return answer
