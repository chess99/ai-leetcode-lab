# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:14Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left, insort
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix) > len(matrix[0]):
            matrix = [list(row) for row in zip(*matrix)]
        rows, columns = len(matrix), len(matrix[0])
        answer = float('-inf')
        for top in range(rows):
            sums = [0] * columns
            for bottom in range(top, rows):
                for column in range(columns):
                    sums[column] += matrix[bottom][column]
                prefixes = [0]
                prefix = 0
                for value in sums:
                    prefix += value
                    index = bisect_left(prefixes, prefix - k)
                    if index < len(prefixes):
                        answer = max(answer, prefix - prefixes[index])
                        if answer == k:
                            return k
                    insort(prefixes, prefix)
        return answer
