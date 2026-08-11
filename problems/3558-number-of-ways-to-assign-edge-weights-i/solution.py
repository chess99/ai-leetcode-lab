# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u - 1].append(v - 1); graph[v - 1].append(u - 1)
        q = deque([0]); depth = [-1] * n; depth[0] = 0
        while q:
            u = q.popleft()
            for v in graph[u]:
                if depth[v] < 0:
                    depth[v] = depth[u] + 1; q.append(v)
        # 深度为 d 的路径中，1/2 赋值的奇数和恰好有 2^(d-1) 种。
        return pow(2, max(depth) - 1, 1_000_000_007)
