# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import deque


class Solution:
    def flipChess(self, chessboard: List[str]) -> int:
        rows, columns = len(chessboard), len(chessboard[0])
        directions = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if dr or dc]
        answer = 0
        for start_row in range(rows):
            for start_column in range(columns):
                if chessboard[start_row][start_column] != '.':
                    continue
                board = [list(row) for row in chessboard]
                board[start_row][start_column] = 'X'
                queue = deque([(start_row, start_column)])
                flipped = 0
                while queue:
                    row, column = queue.popleft()
                    for dr, dc in directions:
                        line = []
                        nr, nc = row + dr, column + dc
                        while 0 <= nr < rows and 0 <= nc < columns and board[nr][nc] == 'O':
                            line.append((nr, nc))
                            nr += dr
                            nc += dc
                        if line and 0 <= nr < rows and 0 <= nc < columns and board[nr][nc] == 'X':
                            for r, c in line:
                                if board[r][c] == 'O':
                                    board[r][c] = 'X'
                                    queue.append((r, c))
                                    flipped += 1
                answer = max(answer, flipped)
        return answer
