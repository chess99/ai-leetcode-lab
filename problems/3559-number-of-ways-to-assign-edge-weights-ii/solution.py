# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1; g = [[] for _ in range(n)]
        for a, b in edges: g[a - 1].append(b - 1); g[b - 1].append(a - 1)
        log = (n + 1).bit_length(); up = [[0] * n for _ in range(log)]; dep = [0] * n; order = [0]
        for u in order:
            for v in g[u]:
                if v != up[0][u]: up[0][v] = u; dep[v] = dep[u] + 1; order.append(v)
        for p in range(1, log):
            for v in range(n): up[p][v] = up[p - 1][up[p - 1][v]]
        def lca(a, b):
            if dep[a] < dep[b]: a, b = b, a
            z = dep[a] - dep[b]
            for p in range(log):
                if z >> p & 1: a = up[p][a]
            if a == b: return a
            for p in range(log - 1, -1,-1):
                if up[p][a] != up[p][b]: a,b=up[p][a],up[p][b]
            return up[0][a]
        mod = 1_000_000_007
        return [0 if (length := dep[a-1]+dep[b-1]-2*dep[lca(a-1,b-1)]) == 0 else pow(2, length-1, mod) for a,b in queries]
