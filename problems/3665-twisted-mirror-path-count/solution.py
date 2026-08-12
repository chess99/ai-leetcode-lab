# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:45Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        vornadexil = grid
        rows, cols = len(vornadexil), len(vornadexil[0])
        mod = 10**9 + 7
        from_left = [[0] * cols for _ in range(rows)]
        from_above = [[0] * cols for _ in range(rows)]
        from_left[0][0] = 1
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    total = 1
                else:
                    total = (from_left[r][c] + from_above[r][c]) % mod
                if vornadexil[r][c] == 0:
                    if c + 1 < cols:
                        from_left[r][c + 1] = (from_left[r][c + 1] + total) % mod
                    if r + 1 < rows:
                        from_above[r + 1][c] = (from_above[r + 1][c] + total) % mod
                else:
                    if r + 1 < rows:
                        from_above[r + 1][c] = (from_above[r + 1][c] + from_left[r][c]) % mod
                    if c + 1 < cols:
                        from_left[r][c + 1] = (from_left[r][c + 1] + from_above[r][c]) % mod
        return (from_left[-1][-1] + from_above[-1][-1]) % mod
