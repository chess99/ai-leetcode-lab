# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:28:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        def dfs(r,c):
            gold=grid[r][c];grid[r][c]=0; best=0
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc=r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]: best=max(best,dfs(nr,nc))
            grid[r][c]=gold
            return gold+best
        return max((dfs(r,c) for r in range(rows) for c in range(cols) if grid[r][c]),default=0)
