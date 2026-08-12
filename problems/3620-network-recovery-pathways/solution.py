# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import deque


class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online); graph = [[] for _ in range(n)]; indeg = [0] * n
        values = set()
        for a, b, w in edges:
            graph[a].append((b, w)); indeg[b] += 1; values.add(w)
        q = deque(i for i in range(n) if not indeg[i]); order = []
        while q:
            u=q.popleft(); order.append(u)
            for v,_ in graph[u]:
                indeg[v]-=1
                if not indeg[v]:q.append(v)
        def possible(limit):
            dp = [10**30] * n; dp[0] = 0
            for u in order:
                if dp[u] > k or (u not in (0,n-1) and not online[u]): continue
                for v,w in graph[u]:
                    if w >= limit and (v == n-1 or online[v]): dp[v] = min(dp[v], dp[u]+w)
            return dp[-1] <= k
        vals = sorted(values); lo, hi = 0, len(vals)-1; ans = -1
        while lo <= hi:
            mid=(lo+hi)//2
            if possible(vals[mid]): ans=vals[mid];lo=mid+1
            else: hi=mid-1
        return ans
