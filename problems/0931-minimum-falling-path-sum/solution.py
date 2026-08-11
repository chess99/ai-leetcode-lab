# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:58:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        previous = matrix[0]
        for row in matrix[1:]:
            current = []
            for column, value in enumerate(row):
                current.append(value + min(previous[max(0, column - 1):column + 2]))
            previous = current
        return min(previous)
