# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:34Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        import heapq
        m,n=len(grid),len(grid[0])
        if m==1 and n==1:return 0
        if (m==1 or grid[1][0]>1) and (n==1 or grid[0][1]>1):return -1
        d=[[10**9]*n for _ in range(m)];d[0][0]=0;q=[(0,0,0)]
        while q:
            t,x,y=heapq.heappop(q)
            if t!=d[x][y]:continue
            if (x,y)==(m-1,n-1):return t
            for a,b in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if 0<=a<m and 0<=b<n:
                    z=max(t+1,grid[a][b])
                    if (z-t)%2==0:z+=1
                    if z<d[a][b]:d[a][b]=z;heapq.heappush(q,(z,a,b))
