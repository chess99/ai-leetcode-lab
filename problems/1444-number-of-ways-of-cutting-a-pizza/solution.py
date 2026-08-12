# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:55Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        rows, columns = len(pizza), len(pizza[0])
        apples = [[0] * (columns + 1) for _ in range(rows + 1)]
        for row in range(rows - 1, -1, -1):
            for column in range(columns - 1, -1, -1):
                apples[row][column] = (apples[row + 1][column] +
                                      apples[row][column + 1] -
                                      apples[row + 1][column + 1] +
                                      (pizza[row][column] == 'A'))

        @lru_cache(None)
        def count(row, column, pieces):
            if apples[row][column] < pieces:
                return 0
            if pieces == 1:
                return 1
            answer = 0
            for next_row in range(row + 1, rows):
                if apples[row][column] > apples[next_row][column]:
                    answer += count(next_row, column, pieces - 1)
            for next_column in range(column + 1, columns):
                if apples[row][column] > apples[row][next_column]:
                    answer += count(row, next_column, pieces - 1)
            return answer % 1_000_000_007

        return count(0, 0, k)
