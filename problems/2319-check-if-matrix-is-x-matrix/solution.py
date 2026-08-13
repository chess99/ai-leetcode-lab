# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:25:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        return all((grid[i][j] != 0) == (i == j or i + j == n - 1) for i in range(n) for j in range(n))
