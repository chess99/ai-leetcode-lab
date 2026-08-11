# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:29Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph=[[] for _ in range(n)]
        for a,b,w in edges:a-=1;b-=1;graph[a].append((b,w));graph[b].append((a,w))
        dist=[float('inf')]*n;dist[-1]=0;heap=[(0,n-1)]
        while heap:
            d,u=heapq.heappop(heap)
            if d!=dist[u]:continue
            for v,w in graph[u]:
                if d+w<dist[v]:dist[v]=d+w;heapq.heappush(heap,(dist[v],v))
        order=sorted(range(n),key=dist.__getitem__);ways=[0]*n;ways[-1]=1
        for u in order:
            for v,_ in graph[u]:
                if dist[v]<dist[u]:ways[u]=(ways[u]+ways[v])%(10**9+7)
        return ways[0]
