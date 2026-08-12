# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, columns = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][column] == 0 for column in range(columns))
        first_column_zero = any(matrix[row][0] == 0 for row in range(rows))
        for row in range(1, rows):
            for column in range(1, columns):
                if matrix[row][column] == 0:
                    matrix[row][0] = 0
                    matrix[0][column] = 0
        for row in range(1, rows):
            for column in range(1, columns):
                if matrix[row][0] == 0 or matrix[0][column] == 0:
                    matrix[row][column] = 0
        if first_row_zero:
            for column in range(columns):
                matrix[0][column] = 0
        if first_column_zero:
            for row in range(rows):
                matrix[row][0] = 0
