# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:00Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        import heapq
        graph=[[]for _ in range(n)]
        for a,b,w in edges:graph[a].append((b,w));graph[b].append((a,w))
        heap=[(0,0)];dist={0:0}
        while heap:
            d,u=heapq.heappop(heap)
            if d!=dist[u]:continue
            for v,w in graph[u]:
                if d+w+1<dist.get(v,float('inf')):dist[v]=d+w+1;heapq.heappush(heap,(d+w+1,v))
        return sum(d<=maxMoves for d in dist.values())+sum(min(w,max(0,maxMoves-dist.get(a,float('inf')))+max(0,maxMoves-dist.get(b,float('inf'))))for a,b,w in edges)
