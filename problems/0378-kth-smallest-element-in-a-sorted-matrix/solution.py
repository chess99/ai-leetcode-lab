# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:50:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            middle = (left + right) // 2; count = 0; row, column = len(matrix) - 1, 0
            while row >= 0 and column < len(matrix):
                if matrix[row][column] <= middle: count += row + 1; column += 1
                else: row -= 1
            if count < k: left = middle + 1
            else: right = middle
        return left
