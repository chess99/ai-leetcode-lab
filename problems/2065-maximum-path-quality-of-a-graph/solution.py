# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        g=[[] for _ in values]
        for a,b,t in edges:g[a].append((b,t));g[b].append((a,t))
        seen=[0]*len(values);ans=0
        def dfs(u,used,score):
            nonlocal ans
            if u==0:ans=max(ans,score)
            for v,t in g[u]:
                if used+t<=maxTime:
                    seen[v]+=1;dfs(v,used+t,score+(values[v] if seen[v]==1 else 0));seen[v]-=1
        seen[0]=1;dfs(0,0,values[0]);return ans
