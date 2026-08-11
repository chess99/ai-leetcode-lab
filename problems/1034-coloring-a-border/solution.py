# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:12:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        original_color = grid[row][col]
        visited = set()
        border = []

        stack = [(row, col)]
        visited.add((row, col))
        while stack:
            r, c = stack.pop()
            same_color_neighbors = 0
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == original_color:
                    same_color_neighbors += 1
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        stack.append((nr, nc))
            if same_color_neighbors < 4:
                border.append((r, c))

        for r, c in border:
            grid[r][c] = color
        return grid
