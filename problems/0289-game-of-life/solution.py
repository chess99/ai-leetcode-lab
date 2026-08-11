# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:44:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, columns = len(board), len(board[0])
        for row in range(rows):
            for column in range(columns):
                live = sum(
                    board[r][c] & 1
                    for r in range(max(0, row - 1), min(rows, row + 2))
                    for c in range(max(0, column - 1), min(columns, column + 2))
                    if (r, c) != (row, column)
                )
                if live == 3 or (board[row][column] == 1 and live == 2):
                    board[row][column] |= 2
        for row in board:
            for column in range(columns):
                row[column] >>= 1
