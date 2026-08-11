# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        grid = [[0]]
        for _ in range(n):
            size = len(grid)
            area = size * size
            next_grid = [[0] * (size * 2) for _ in range(size * 2)]
            for r in range(size):
                for c in range(size):
                    value = grid[r][c]
                    next_grid[r][c] = value + 3 * area
                    next_grid[r][c + size] = value
                    next_grid[r + size][c] = value + 2 * area
                    next_grid[r + size][c + size] = value + area
            grid = next_grid
        return grid
