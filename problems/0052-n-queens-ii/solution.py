# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:54Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        def search(row: int, columns: int, diagonals1: int, diagonals2: int) -> None:
            nonlocal count
            if row == n:
                count += 1
                return
            available = ((1 << n) - 1) & ~(columns | diagonals1 | diagonals2)
            while available:
                bit = available & -available
                available -= bit
                search(row + 1, columns | bit, (diagonals1 | bit) << 1,
                       (diagonals2 | bit) >> 1)
        search(0, 0, 0, 0)
        return count
