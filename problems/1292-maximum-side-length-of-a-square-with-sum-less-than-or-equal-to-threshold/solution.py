# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:37:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows, cols = len(mat), len(mat[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for row in range(rows):
            for col in range(cols):
                prefix[row + 1][col + 1] = (mat[row][col] + prefix[row][col + 1]
                                             + prefix[row + 1][col] - prefix[row][col])

        def exists(side: int) -> bool:
            for row in range(side, rows + 1):
                for col in range(side, cols + 1):
                    total = (prefix[row][col] - prefix[row - side][col]
                             - prefix[row][col - side] + prefix[row - side][col - side])
                    if total <= threshold:
                        return True
            return False

        left, right = 0, min(rows, cols)
        while left < right:
            middle = (left + right + 1) // 2
            if exists(middle):
                left = middle
            else:
                right = middle - 1
        return left
