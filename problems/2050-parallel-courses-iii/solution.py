# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:06Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        from collections import deque
        g=[[] for _ in range(n)];deg=[0]*n
        for a,b in relations:g[a-1].append(b-1);deg[b-1]+=1
        dp=time[:];q=deque(i for i in range(n) if not deg[i])
        while q:
            u=q.popleft()
            for v in g[u]:
                dp[v]=max(dp[v],dp[u]+time[v]);deg[v]-=1
                if not deg[v]:q.append(v)
        return max(dp)
