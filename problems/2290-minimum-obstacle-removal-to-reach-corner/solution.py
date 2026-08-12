# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        from collections import deque
        m,n=len(grid),len(grid[0]);d=[[10**9]*n for _ in range(m)];d[0][0]=0;q=deque([(0,0)])
        while q:
            x,y=q.popleft()
            for a,b in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if 0<=a<m and 0<=b<n and d[a][b]>d[x][y]+grid[a][b]:
                    d[a][b]=d[x][y]+grid[a][b]
                    (q.appendleft if grid[a][b]==0 else q.append)((a,b))
        return d[-1][-1]
