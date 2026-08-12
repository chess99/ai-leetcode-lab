# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:07Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        active = set(map(tuple, lamps))
        rows = Counter(row for row, column in active)
        columns = Counter(column for row, column in active)
        diagonals = Counter(row - column for row, column in active)
        anti_diagonals = Counter(row + column for row, column in active)
        answer = []
        for row, column in queries:
            answer.append(int(bool(rows[row] or columns[column] or diagonals[row-column]
                                   or anti_diagonals[row+column])))
            for next_row in range(max(0, row - 1), min(n, row + 2)):
                for next_column in range(max(0, column - 1), min(n, column + 2)):
                    if (next_row, next_column) in active:
                        active.remove((next_row, next_column))
                        rows[next_row] -= 1
                        columns[next_column] -= 1
                        diagonals[next_row - next_column] -= 1
                        anti_diagonals[next_row + next_column] -= 1
        return answer
