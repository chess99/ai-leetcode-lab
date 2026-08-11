# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:24:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, columns = len(board), len(board[0])

        def mark(row: int, column: int) -> None:
            stack = [(row, column)]
            while stack:
                r, c = stack.pop()
                if not (0 <= r < rows and 0 <= c < columns) or board[r][c] != "O":
                    continue
                board[r][c] = "#"
                stack.extend(((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)))

        for row in range(rows):
            mark(row, 0)
            mark(row, columns - 1)
        for column in range(columns):
            mark(0, column)
            mark(rows - 1, column)

        for row in range(rows):
            for column in range(columns):
                if board[row][column] == "O":
                    board[row][column] = "X"
                elif board[row][column] == "#":
                    board[row][column] = "O"
