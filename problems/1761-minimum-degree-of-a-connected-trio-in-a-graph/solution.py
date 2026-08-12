# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:42Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        g=[set()for _ in range(n)];deg=[0]*n
        for a,b in edges:a-=1;b-=1;g[a].add(b);g[b].add(a);deg[a]+=1;deg[b]+=1
        ans=10**9
        for a in range(n):
            for b in g[a]:
                if b>a:
                    for c in g[a]&g[b]:
                        if c>b:ans=min(ans,deg[a]+deg[b]+deg[c]-6)
        return -1 if ans==10**9 else ans
