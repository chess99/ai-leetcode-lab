# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)

        down = [0] * n
        for node in reversed(order):
            for child in graph[node]:
                if parent[child] == node:
                    down[node] = max(down[node], (1 if child & 1 else 2) + down[child])

        up = [0] * n
        for node in order:
            best_value = second_value = -1
            best_child = -1
            for child in graph[node]:
                if parent[child] != node:
                    continue
                value = (1 if child & 1 else 2) + down[child]
                if value > best_value:
                    second_value = best_value
                    best_value = value
                    best_child = child
                elif value > second_value:
                    second_value = value

            enter_parent = 1 if node & 1 else 2
            for child in graph[node]:
                if parent[child] != node:
                    continue
                sibling_best = second_value if child == best_child else best_value
                up[child] = enter_parent + max(0, up[node], sibling_best)

        return [max(down[node], up[node]) for node in range(n)]
