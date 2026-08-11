# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:43:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        connections = {
            1: ((0, -1), (0, 1)),
            2: ((-1, 0), (1, 0)),
            3: ((0, -1), (1, 0)),
            4: ((0, 1), (1, 0)),
            5: ((0, -1), (-1, 0)),
            6: ((0, 1), (-1, 0)),
        }
        rows, cols = len(grid), len(grid[0])
        stack = [(0, 0)]
        seen = {(0, 0)}
        while stack:
            row, col = stack.pop()
            if row == rows - 1 and col == cols - 1:
                return True
            for dr, dc in connections[grid[row][col]]:
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen
                        and (-dr, -dc) in connections[grid[nr][nc]]):
                    seen.add((nr, nc))
                    stack.append((nr, nc))
        return False
