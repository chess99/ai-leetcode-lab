# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        size = len(board)
        for row in range(size):
            for column in range(size):
                if board[0][0] ^ board[row][0] ^ board[0][column] ^ board[row][column]:
                    return -1
        row_sum = sum(board[0])
        column_sum = sum(board[row][0] for row in range(size))
        if row_sum not in (size // 2, (size + 1) // 2):
            return -1
        if column_sum not in (size // 2, (size + 1) // 2):
            return -1
        row_mismatch = sum(board[0][column] == column % 2 for column in range(size))
        column_mismatch = sum(board[row][0] == row % 2 for row in range(size))
        if size % 2:
            if row_mismatch % 2:
                row_mismatch = size - row_mismatch
            if column_mismatch % 2:
                column_mismatch = size - column_mismatch
        else:
            row_mismatch = min(row_mismatch, size - row_mismatch)
            column_mismatch = min(column_mismatch, size - column_mismatch)
        return (row_mismatch + column_mismatch) // 2
