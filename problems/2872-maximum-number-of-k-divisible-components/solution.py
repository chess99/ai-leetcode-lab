# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
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
        remainder = [value % k for value in values]
        answer = 0
        for node in reversed(order):
            if remainder[node] == 0:
                answer += 1
            elif parent[node] != -1:
                remainder[parent[node]] = (remainder[parent[node]] + remainder[node]) % k
        return answer
