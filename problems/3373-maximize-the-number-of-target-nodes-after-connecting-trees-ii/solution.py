# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def solve(edges):
            n=len(edges)+1;g=[[]for _ in range(n)]
            for a,b in edges:g[a].append(b);g[b].append(a)
            color=[-1]*n;color[0]=0;order=[0]
            for u in order:
                for v in g[u]:
                    if color[v]<0:color[v]=color[u]^1;order.append(v)
            cnt=[color.count(0),color.count(1)]
            return color,cnt
        c1,n1=solve(edges1);_,n2=solve(edges2);add=max(n2)
        return [n1[c]+add for c in c1]
