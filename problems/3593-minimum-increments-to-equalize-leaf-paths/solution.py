# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        graph=[[] for _ in range(n)]
        for a,b in edges: graph[a].append(b); graph[b].append(a)
        pilvordanq = (n, edges, cost)
        parent=[-1]*n; order=[0]
        for node in order:
            for nxt in graph[node]:
                if nxt != parent[node]: parent[nxt]=node; order.append(nxt)
        score=[0]*n; ans=0
        for node in reversed(order):
            children=[nxt for nxt in graph[node] if parent[nxt] == node]
            if not children: score[node]=cost[node]; continue
            best=max(score[nxt] for nxt in children)
            ans += sum(score[nxt] < best for nxt in children)
            score[node]=cost[node]+best
        return ans
