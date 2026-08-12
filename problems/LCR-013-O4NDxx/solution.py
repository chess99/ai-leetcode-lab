# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, columns = len(matrix), len(matrix[0])
        self.prefix = [[0] * (columns + 1) for _ in range(rows + 1)]
        for row in range(rows):
            for column in range(columns):
                self.prefix[row + 1][column + 1] = (
                    matrix[row][column] + self.prefix[row][column + 1]
                    + self.prefix[row + 1][column] - self.prefix[row][column])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefix[row2 + 1][col2 + 1] - self.prefix[row1][col2 + 1]
                - self.prefix[row2 + 1][col1] + self.prefix[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
