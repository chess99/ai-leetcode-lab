# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        rows, columns = len(matrix), len(matrix[0])
        answer = [0, 0, 0, 0]
        best_sum = float("-inf")
        for top in range(rows):
            column_sums = [0] * columns
            for bottom in range(top, rows):
                for column in range(columns):
                    column_sums[column] += matrix[bottom][column]
                current_sum = 0
                left = 0
                for right, value in enumerate(column_sums):
                    if current_sum <= 0:
                        current_sum = value
                        left = right
                    else:
                        current_sum += value
                    if current_sum > best_sum:
                        best_sum = current_sum
                        answer = [top, left, bottom, right]
        return answer
