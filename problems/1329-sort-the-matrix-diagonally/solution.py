# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:39:58Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = defaultdict(list)
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                diagonals[row - col].append(mat[row][col])
        for values in diagonals.values():
            values.sort(reverse=True)
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                mat[row][col] = diagonals[row - col].pop()
        return mat
