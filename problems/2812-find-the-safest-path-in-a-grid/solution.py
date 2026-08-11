# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:15Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from heapq import heappop,heappush
from typing import List
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n=len(grid); q=deque(); dist=[[-1]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j]:dist[i][j]=0;q.append((i,j))
        while q:
            i,j=q.popleft()
            for a,b in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=a<n and 0<=b<n and dist[a][b]<0:dist[a][b]=dist[i][j]+1;q.append((a,b))
        heap=[(-dist[0][0],0,0)]; seen={(0,0)}
        while heap:
            safe,i,j=heappop(heap); safe=-safe
            if (i,j)==(n-1,n-1):return safe
            for a,b in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=a<n and 0<=b<n and (a,b) not in seen:seen.add((a,b));heappush(heap,(-min(safe,dist[a][b]),a,b))
