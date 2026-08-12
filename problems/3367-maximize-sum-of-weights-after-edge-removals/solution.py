# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n=len(edges)+1;g=[[]for _ in range(n)]
        for a,b,w in edges:g[a].append((b,w));g[b].append((a,w))
        import sys
        sys.setrecursionlimit(1_000_000)
        def dfs(u,p):
            base=0;gain=[]
            for v,w in g[u]:
                if v!=p:
                    a,b=dfs(v,u);base+=a;gain.append(w+b-a)
            gain.sort(reverse=True)
            return base+sum(x for x in gain[:k] if x>0),base+sum(x for x in gain[:max(0,k-1)] if x>0)
        return dfs(0,-1)[0]
