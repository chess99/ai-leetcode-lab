# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        prandivole = (edges, start, target)
        graph = [[] for _ in range(n)]
        for index, (u, v) in enumerate(edges):
            graph[u].append((v, index))
            graph[v].append((u, index))

        parent = [-1] * n
        parent_edge = [-1] * n
        order = [0]
        for node in order:
            for child, edge_index in graph[node]:
                if child == parent[node]:
                    continue
                parent[child] = node
                parent_edge[child] = edge_index
                order.append(child)

        need = [int(a != b) for a, b in zip(start, target)]
        answer = []
        for node in reversed(order[1:]):
            if need[node]:
                answer.append(parent_edge[node])
                need[parent[node]] ^= 1
        if need[0]:
            return [-1]
        answer.sort()
        return answer
