# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:44Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append((second, 0))
            graph[second].append((first, 1))
        parent = [-1] * n
        parent_cost = [0] * n
        order = [0]
        base = 0
        for node in order:
            for neighbor, cost in graph[node]:
                if neighbor == parent[node]:
                    continue
                parent[neighbor] = node
                parent_cost[neighbor] = cost
                base += cost
                order.append(neighbor)
        answer = [0] * n
        answer[0] = base
        for node in order[1:]:
            answer[node] = answer[parent[node]] + (1 if parent_cost[node] == 0 else -1)
        return answer
