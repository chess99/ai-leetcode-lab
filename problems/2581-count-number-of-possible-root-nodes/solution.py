# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        g=[[]for _ in range(len(edges)+1)]
        for a,b in edges:g[a].append(b);g[b].append(a)
        gs=set(map(tuple,guesses));parent=[-1]*len(g);order=[0]
        for u in order:
            for v in g[u]:
                if v!=parent[u]:parent[v]=u;order.append(v)
        cur=sum((parent[v],v)in gs for v in range(1,len(g)));ans=0
        stack=[(0,-1,cur)]
        while stack:
            u,p,value=stack.pop();ans+=value>=k
            for v in g[u]:
                if v!=p:
                    stack.append((v,u,value-((u,v) in gs)+((v,u) in gs)))
        return ans
