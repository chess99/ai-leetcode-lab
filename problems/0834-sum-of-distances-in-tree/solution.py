# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(n)]
        for a,b in edges:graph[a].append(b);graph[b].append(a)
        parent=[-1]*n;order=[0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor!=parent[node]:parent[neighbor]=node;order.append(neighbor)
        count=[1]*n;answer=[0]*n
        for node in reversed(order[1:]):count[parent[node]]+=count[node];answer[parent[node]]+=answer[node]+count[node]
        for node in order[1:]:answer[node]=answer[parent[node]]-count[node]+(n-count[node])
        return answer
