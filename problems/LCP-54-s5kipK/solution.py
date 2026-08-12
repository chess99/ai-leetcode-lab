# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:49Z
# Experiment: ai-leetcode-lab, round 1
import sys
from typing import List


class Solution:
    def minimumCost(self, cost: List[int], roads: List[List[int]]) -> int:
        n = len(cost)
        graph = [[] for _ in range(n)]
        for edge_id, (left, right) in enumerate(roads):
            graph[left].append((right, edge_id))
            graph[right].append((left, edge_id))

        sys.setrecursionlimit(max(1000, n * 3))
        discovery = [0] * n
        low = [0] * n
        articulation = [False] * n
        edge_stack = []
        components = []
        clock = 0

        def dfs(node: int, parent_edge: int) -> None:
            nonlocal clock
            clock += 1
            discovery[node] = low[node] = clock
            child_count = 0
            for neighbor, edge_id in graph[node]:
                if not discovery[neighbor]:
                    child_count += 1
                    edge_stack.append(edge_id)
                    dfs(neighbor, edge_id)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] >= discovery[node]:
                        if parent_edge != -1 or child_count > 1:
                            articulation[node] = True
                        vertices = set()
                        while True:
                            popped = edge_stack.pop()
                            vertices.update(roads[popped])
                            if popped == edge_id:
                                break
                        components.append(vertices)
                elif edge_id != parent_edge and discovery[neighbor] < discovery[node]:
                    edge_stack.append(edge_id)
                    low[node] = min(low[node], discovery[neighbor])

        dfs(0, -1)
        if len(components) == 1:
            return min(cost)

        leaf_costs = []
        for component in components:
            cut_count = sum(articulation[node] for node in component)
            if cut_count == 1:
                leaf_costs.append(min(cost[node] for node in component if not articulation[node]))
        return sum(leaf_costs) - max(leaf_costs)
