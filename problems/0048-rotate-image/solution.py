# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:12:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for row in range(n):
            for column in range(row + 1, n):
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
        for row in matrix:
            row.reverse()
