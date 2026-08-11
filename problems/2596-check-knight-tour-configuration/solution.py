# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:27Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        if grid[0][0] != 0:
            return False
        positions = [None] * (n * n)
        for row in range(n):
            for col in range(n):
                positions[grid[row][col]] = (row, col)
        for step in range(1, n * n):
            r1, c1 = positions[step - 1]
            r2, c2 = positions[step]
            if sorted((abs(r1 - r2), abs(c1 - c2))) != [1, 2]:
                return False
        return True
