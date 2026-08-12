# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        g=[[]for _ in range(n)]
        for a,b in edges:g[a].append(b);g[b].append(a)
        cnt=[0]*n
        def path(u,p,t):
            if u==t:cnt[u]+=1;return True
            for v in g[u]:
                if v!=p and path(v,u,t):cnt[u]+=1;return True
            return False
        for a,b in trips:path(a,-1,b)
        def dp(u,p):
            full=cnt[u]*price[u];half=full//2
            for v in g[u]:
                if v!=p:
                    a,b=dp(v,u);full+=min(a,b);half+=a
            return full,half
        return min(dp(0,-1))
