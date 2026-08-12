# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        from collections import deque
        g=[[]for _ in range(n)]
        for a,b in edges:g[a].append(b);g[b].append(a)
        ans=10**9
        for s in range(n):
            d=[-1]*n;d[s]=0;q=deque([(s,-1)])
            while q:
                u,p=q.popleft()
                for v in g[u]:
                    if d[v]<0:d[v]=d[u]+1;q.append((v,u))
                    elif v!=p:ans=min(ans,d[u]+d[v]+1)
        return ans if ans<10**9 else -1
