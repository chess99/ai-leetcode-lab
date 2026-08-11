# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:16:02Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, columns = len(matrix), len(matrix[0])
        first_column_zero = any(matrix[row][0] == 0 for row in range(rows))

        for row in range(rows):
            for column in range(1, columns):
                if matrix[row][column] == 0:
                    matrix[row][0] = 0
                    matrix[0][column] = 0

        for row in range(rows - 1, -1, -1):
            for column in range(columns - 1, 0, -1):
                if matrix[row][0] == 0 or matrix[0][column] == 0:
                    matrix[row][column] = 0
            if first_column_zero:
                matrix[row][0] = 0
