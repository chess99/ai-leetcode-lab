# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for row in range(size):
            for column in range(row + 1, size):
                matrix[row][column], matrix[column][row] = (
                    matrix[column][row], matrix[row][column]
                )
        for row in matrix:
            row.reverse()
