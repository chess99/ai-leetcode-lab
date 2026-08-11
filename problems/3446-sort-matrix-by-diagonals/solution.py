# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        for row in range(n):
            vals=[grid[row+i][i] for i in range(n-row)]; vals.sort(reverse=True)
            for i,v in enumerate(vals): grid[row+i][i]=v
        for col in range(1,n):
            vals=[grid[i][col+i] for i in range(n-col)]; vals.sort()
            for i,v in enumerate(vals): grid[i][col+i]=v
        return grid
