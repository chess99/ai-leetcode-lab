# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:46:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x = sum(row.count('X') for row in board); o = sum(row.count('O') for row in board)
        wins = lambda p: any(all(board[r][c] == p for c in range(3)) for r in range(3)) or any(all(board[r][c] == p for r in range(3)) for c in range(3)) or all(board[i][i] == p for i in range(3)) or all(board[i][2-i] == p for i in range(3))
        return o <= x <= o + 1 and (not wins('X') or x == o + 1) and (not wins('O') or x == o)
