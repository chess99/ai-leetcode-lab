# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:37:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def flood(row, col):
            stack = [(row, col)]
            grid[row][col] = 1
            while stack:
                r, c = stack.pop()
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        stack.append((nr,nc))
        for row in range(rows):
            for col in (0, cols - 1):
                if grid[row][col] == 0: flood(row, col)
        for col in range(cols):
            for row in (0, rows - 1):
                if grid[row][col] == 0: flood(row, col)
        answer = 0
        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if grid[row][col] == 0:
                    answer += 1
                    flood(row, col)
        return answer
