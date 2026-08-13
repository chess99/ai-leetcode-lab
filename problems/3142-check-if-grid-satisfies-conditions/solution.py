# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:45:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if row + 1 < rows and grid[row][col] != grid[row + 1][col]:
                    return False
                if col + 1 < cols and grid[row][col] == grid[row][col + 1]:
                    return False
        return True
