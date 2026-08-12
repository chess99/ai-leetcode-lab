# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
        parent = [-1] * n
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)

        with_leaf = [0] * n
        without_leaf = [0] * n
        answer = 0
        for node in reversed(order):
            with_leaf[node] = price[node]
            for neighbor in graph[node]:
                if parent[neighbor] != node:
                    continue
                answer = max(
                    answer,
                    with_leaf[node] + without_leaf[neighbor],
                    without_leaf[node] + with_leaf[neighbor],
                )
                with_leaf[node] = max(
                    with_leaf[node], price[node] + with_leaf[neighbor]
                )
                without_leaf[node] = max(
                    without_leaf[node], price[node] + without_leaf[neighbor]
                )
        return answer
