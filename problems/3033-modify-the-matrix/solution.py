# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:41:21Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for column in range(len(matrix[0])):
            maximum = max(row[column] for row in matrix)
            for row in matrix:
                if row[column] == -1:
                    row[column] = maximum
        return matrix
