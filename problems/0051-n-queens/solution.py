# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        columns, diagonals1, diagonals2 = set(), set(), set()
        positions = [-1] * n
        def place(row: int) -> None:
            if row == n:
                result.append(["." * col + "Q" + "." * (n - col - 1) for col in positions])
                return
            for col in range(n):
                if col in columns or row - col in diagonals1 or row + col in diagonals2:
                    continue
                positions[row] = col
                columns.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)
                place(row + 1)
                columns.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)
        place(0)
        return result
