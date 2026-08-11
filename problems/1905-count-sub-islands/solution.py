# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:47:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows,cols=len(grid1),len(grid1[0]);answer=0
        for r in range(rows):
            for c in range(cols):
                if not grid2[r][c]:continue
                stack=[(r,c)];grid2[r][c]=0;valid=True
                while stack:
                    x,y=stack.pop();valid&=bool(grid1[x][y])
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<rows and 0<=ny<cols and grid2[nx][ny]:grid2[nx][ny]=0;stack.append((nx,ny))
                answer+=valid
        return answer
