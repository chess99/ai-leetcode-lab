# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        order = [0]
        for node in order:
            for other in graph[node]:
                if other != parent[node]:
                    parent[other] = node
                    order.append(other)

        down = [1 if value else -1 for value in good]
        for node in reversed(order[1:]):
            down[parent[node]] += max(0, down[node])

        answer = down[:]
        for node in order[1:]:
            contribution_from_parent = answer[parent[node]] - max(0, down[node])
            answer[node] = down[node] + max(0, contribution_from_parent)
        return answer
