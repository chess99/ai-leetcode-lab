# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:11:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, columns = len(mat), len(mat[0])
        result = []
        for diagonal in range(rows + columns - 1):
            row = min(diagonal, rows - 1)
            column = diagonal - row
            values = []
            while row >= 0 and column < columns:
                values.append(mat[row][column])
                row -= 1
                column += 1
            if diagonal % 2 == 0:
                result.extend(values)
            else:
                result.extend(reversed(values))
        return result
