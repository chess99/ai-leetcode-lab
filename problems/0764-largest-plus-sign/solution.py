# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:41:42Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        order = [[n] * n for _ in range(n)]
        for row, column in mines:
            order[row][column] = 0

        for row in range(n):
            run = 0
            for column in range(n):
                run = run + 1 if order[row][column] else 0
                order[row][column] = min(order[row][column], run)
            run = 0
            for column in range(n - 1, -1, -1):
                run = run + 1 if order[row][column] else 0
                order[row][column] = min(order[row][column], run)

        largest = 0
        for column in range(n):
            run = 0
            for row in range(n):
                run = run + 1 if order[row][column] else 0
                order[row][column] = min(order[row][column], run)
            run = 0
            for row in range(n - 1, -1, -1):
                run = run + 1 if order[row][column] else 0
                order[row][column] = min(order[row][column], run)
                largest = max(largest, order[row][column])

        return largest
