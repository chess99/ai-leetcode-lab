# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        components = n
        for u, v, weight in sorted(edges, key=lambda edge: edge[2]):
            a, b = find(u), find(v)
            if a != b:
                parent[b] = a; components -= 1
                if components == k: return weight
        return 0
