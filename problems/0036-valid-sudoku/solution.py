# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:10:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in range(9):
            for column in range(9):
                value = board[row][column]
                if value == ".":
                    continue
                row_key = ("row", row, value)
                column_key = ("column", column, value)
                box_key = ("box", row // 3, column // 3, value)
                if row_key in seen or column_key in seen or box_key in seen:
                    return False
                seen.add(row_key)
                seen.add(column_key)
                seen.add(box_key)
        return True
