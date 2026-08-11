# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:10Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph=[[] for _ in range(n)]
        for a,b,t in roads:graph[a].append((b,t));graph[b].append((a,t))
        dist=[float('inf')]*n;ways=[0]*n;dist[0]=0;ways[0]=1;heap=[(0,0)]
        while heap:
            d,u=heapq.heappop(heap)
            if d!=dist[u]:continue
            for v,w in graph[u]:
                if d+w<dist[v]:dist[v]=d+w;ways[v]=ways[u];heapq.heappush(heap,(dist[v],v))
                elif d+w==dist[v]:ways[v]=(ways[v]+ways[u])%(10**9+7)
        return ways[-1]
