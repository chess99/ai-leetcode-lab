# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:10:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0]);stack=[]
        for r in range(rows): stack += [(r,0),(r,cols-1)]
        for c in range(cols): stack += [(0,c),(rows-1,c)]
        while stack:
            r,c=stack.pop()
            if not(0<=r<rows and 0<=c<cols) or grid[r][c]!=1:continue
            grid[r][c]=0;stack += [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
        return sum(map(sum,grid))
