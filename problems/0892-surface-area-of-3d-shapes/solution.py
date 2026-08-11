# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:09:02Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        area = 0
        for r, row in enumerate(grid):
            for c, height in enumerate(row):
                if height:
                    area += 2 + 4 * height
                    if r: area -= 2 * min(height, grid[r - 1][c])
                    if c: area -= 2 * min(height, grid[r][c - 1])
        return area
