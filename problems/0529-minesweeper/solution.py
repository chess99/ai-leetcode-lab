# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:14:03Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, columns = len(board), len(board[0])
        row, column = click
        if board[row][column] == "M":
            board[row][column] = "X"
            return board

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1),
        ]
        queue = deque([(row, column)])
        while queue:
            row, column = queue.popleft()
            if board[row][column] != "E":
                continue

            adjacent_mines = 0
            neighbors = []
            for row_delta, column_delta in directions:
                next_row = row + row_delta
                next_column = column + column_delta
                if 0 <= next_row < rows and 0 <= next_column < columns:
                    if board[next_row][next_column] == "M":
                        adjacent_mines += 1
                    elif board[next_row][next_column] == "E":
                        neighbors.append((next_row, next_column))

            if adjacent_mines:
                board[row][column] = str(adjacent_mines)
            else:
                board[row][column] = "B"
                queue.extend(neighbors)

        return board
