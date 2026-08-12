# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid);sizes={0:0};label=2
        for r in range(n):
            for c in range(n):
                if grid[r][c]!=1:continue
                grid[r][c]=label;stack=[(r,c)];area=0
                while stack:
                    x,y=stack.pop();area+=1
                    for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                        if 0<=nx<n and 0<=ny<n and grid[nx][ny]==1:grid[nx][ny]=label;stack.append((nx,ny))
                sizes[label]=area;label+=1
        answer=max(sizes.values())
        for r in range(n):
            for c in range(n):
                if grid[r][c]==0:
                    neighbors={grid[x][y] for x,y in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)) if 0<=x<n and 0<=y<n}
                    answer=max(answer,1+sum(sizes[x] for x in neighbors))
        return answer
