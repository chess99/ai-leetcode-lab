# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        opponent = "W" if color == "B" else "B"

        for row_step, column_step in (
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),            (0, 1),
            (1, -1),  (1, 0),   (1, 1),
        ):
            row, column = rMove + row_step, cMove + column_step
            opponent_count = 0

            while 0 <= row < 8 and 0 <= column < 8 and board[row][column] == opponent:
                opponent_count += 1
                row += row_step
                column += column_step

            if (
                opponent_count > 0
                and 0 <= row < 8
                and 0 <= column < 8
                and board[row][column] == color
            ):
                return True

        return False
