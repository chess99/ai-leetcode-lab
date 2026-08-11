# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:16:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def search(row: int, col: int, index: int) -> bool:
            if index == len(word):
                return True
            if (
                row < 0
                or row == rows
                or col < 0
                or col == cols
                or board[row][col] != word[index]
            ):
                return False

            char = board[row][col]
            board[row][col] = "#"
            found = (
                search(row + 1, col, index + 1)
                or search(row - 1, col, index + 1)
                or search(row, col + 1, index + 1)
                or search(row, col - 1, index + 1)
            )
            board[row][col] = char
            return found

        return any(search(row, col, 0) for row in range(rows) for col in range(cols))
