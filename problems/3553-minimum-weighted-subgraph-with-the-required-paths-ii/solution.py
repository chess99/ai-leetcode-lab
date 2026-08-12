# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w)); graph[v].append((u, w))
        log = (n + 1).bit_length()
        up = [[0] * n for _ in range(log)]
        depth = [0] * n; dist = [0] * n; order = [0]
        for u in order:
            for v, w in graph[u]:
                if v != up[0][u]:
                    up[0][v] = u; depth[v] = depth[u] + 1; dist[v] = dist[u] + w; order.append(v)
        for p in range(1, log):
            for v in range(n): up[p][v] = up[p - 1][up[p - 1][v]]
        def lca(a, b):
            if depth[a] < depth[b]: a, b = b, a
            delta = depth[a] - depth[b]
            for p in range(log):
                if delta >> p & 1: a = up[p][a]
            if a == b: return a
            for p in range(log - 1, -1, -1):
                if up[p][a] != up[p][b]: a, b = up[p][a], up[p][b]
            return up[0][a]
        def d(a, b): return dist[a] + dist[b] - 2 * dist[lca(a, b)]
        return [(d(a, b) + d(a, c) + d(b, c)) // 2 for a, b, c in queries]
