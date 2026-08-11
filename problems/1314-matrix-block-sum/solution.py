# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:39:21Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]

        def area(row1: int, col1: int, row2: int, col2: int) -> int:
            return prefix[row2][col2] - prefix[row1][col2] - prefix[row2][col1] + prefix[row1][col1]

        return [
            [area(max(0, r - k), max(0, c - k), min(rows, r + k + 1), min(cols, c + k + 1)) for c in range(cols)]
            for r in range(rows)
        ]
