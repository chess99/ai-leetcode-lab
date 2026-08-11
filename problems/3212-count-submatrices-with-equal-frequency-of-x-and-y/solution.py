# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        x_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        y_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        answer = 0
        for row in range(rows):
            for col in range(cols):
                x_sum[row + 1][col + 1] = x_sum[row][col + 1] + x_sum[row + 1][col] - x_sum[row][col] + (grid[row][col] == 'X')
                y_sum[row + 1][col + 1] = y_sum[row][col + 1] + y_sum[row + 1][col] - y_sum[row][col] + (grid[row][col] == 'Y')
                if x_sum[row + 1][col + 1] and x_sum[row + 1][col + 1] == y_sum[row + 1][col + 1]:
                    answer += 1
        return answer
