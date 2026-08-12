# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:06Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        from collections import deque
        g=[[] for _ in range(n)]
        for a,b in edges:g[a-1].append(b-1);g[b-1].append(a-1)
        dist=[[10**9,10**9] for _ in range(n)];dist[0][0]=0;q=deque([(0,0)])
        while q:
            u,d=q.popleft()
            for v in g[u]:
                nd=d+1
                if nd<dist[v][0]:dist[v][1]=dist[v][0];dist[v][0]=nd;q.append((v,nd))
                elif dist[v][0]<nd<dist[v][1]:dist[v][1]=nd;q.append((v,nd))
        steps=dist[-1][1]; now=0
        for _ in range(steps):
            if (now//change)%2:now=(now//change+1)*change
            now+=time
        return now
