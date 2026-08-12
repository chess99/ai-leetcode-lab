# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:22:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        size = len(matrix)
        right = [[0] * (size + 1) for _ in range(size + 1)]
        down = [[0] * (size + 1) for _ in range(size + 1)]
        for row in range(size - 1, -1, -1):
            for col in range(size - 1, -1, -1):
                if matrix[row][col] == 0:
                    right[row][col] = right[row][col + 1] + 1
                    down[row][col] = down[row + 1][col] + 1
        for side in range(size, 0, -1):
            for row in range(size - side + 1):
                for col in range(size - side + 1):
                    if (right[row][col] >= side and down[row][col] >= side
                            and right[row + side - 1][col] >= side
                            and down[row][col + side - 1] >= side):
                        return [row, col, side]
        return []
