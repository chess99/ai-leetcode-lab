# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:53:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ships = 0
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == "X" and (row == 0 or board[row - 1][column] != "X") and (column == 0 or board[row][column - 1] != "X"):
                    ships += 1
        return ships
