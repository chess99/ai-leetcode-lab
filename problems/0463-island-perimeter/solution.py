# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:40:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell:
                    perimeter += 4
                    if r > 0 and grid[r - 1][c]:
                        perimeter -= 2
                    if c > 0 and grid[r][c - 1]:
                        perimeter -= 2
        return perimeter
