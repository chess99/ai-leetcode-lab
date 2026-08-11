# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0]); ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    total=grid[i][j]; stack=[(i,j)]; grid[i][j]=0
                    while stack:
                        x,y=stack.pop()
                        for a,b in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                            if 0<=a<m and 0<=b<n and grid[a][b]:
                                total+=grid[a][b]; grid[a][b]=0; stack.append((a,b))
                    if total%k==0: ans+=1
        return ans
