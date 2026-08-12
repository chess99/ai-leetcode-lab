# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:33Z
# Experiment: ai-leetcode-lab, round 1
from heapq import nlargest
from typing import List


class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        rows, cols = len(board), len(board[0])
        negative = -10**30

        suffix: list[list[tuple[int, int]]] = [[] for _ in range(rows)]
        best_by_col = [negative] * cols
        for row in range(rows - 1, -1, -1):
            suffix[row] = nlargest(3, ((value, col) for col, value in enumerate(best_by_col)))
            for col, value in enumerate(board[row]):
                best_by_col[col] = max(best_by_col[col], value)

        answer = negative
        best_by_col = [negative] * cols
        for row in range(rows):
            prefix = nlargest(3, ((value, col) for col, value in enumerate(best_by_col)))
            for middle_col, middle_value in enumerate(board[row]):
                for first_value, first_col in prefix:
                    if first_col == middle_col:
                        continue
                    for third_value, third_col in suffix[row]:
                        if third_col != middle_col and third_col != first_col:
                            answer = max(answer, first_value + middle_value + third_value)
            for col, value in enumerate(board[row]):
                best_by_col[col] = max(best_by_col[col], value)
        return answer
