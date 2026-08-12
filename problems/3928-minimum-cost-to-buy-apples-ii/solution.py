# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        import heapq
        g=[[]for _ in range(n)]
        for a,b,c,t in roads:
            w=c*(t+1);g[a].append((b,w));g[b].append((a,w))
        d=prices[:];q=[(d[i],i)for i in range(n)];heapq.heapify(q)
        while q:
            x,u=heapq.heappop(q)
            if x!=d[u]:continue
            for v,w in g[u]:
                if x+w<d[v]:d[v]=x+w;heapq.heappush(q,(d[v],v))
        return d
