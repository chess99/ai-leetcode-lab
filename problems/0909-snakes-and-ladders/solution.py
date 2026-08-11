# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:56:17Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        size = len(board)

        def coordinates(square: int) -> tuple[int, int]:
            quotient, remainder = divmod(square - 1, size)
            row = size - 1 - quotient
            column = remainder if quotient % 2 == 0 else size - 1 - remainder
            return row, column

        queue = deque([(1, 0)])
        visited = {1}
        while queue:
            square, moves = queue.popleft()
            if square == size * size:
                return moves
            for next_square in range(square + 1, min(square + 6, size * size) + 1):
                row, column = coordinates(next_square)
                destination = board[row][column] if board[row][column] != -1 else next_square
                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, moves + 1))
        return -1
