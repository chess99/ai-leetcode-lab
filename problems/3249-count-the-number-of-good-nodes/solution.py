# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)
        parent = [-1] * n
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)
        size = [1] * n
        answer = 0
        for node in reversed(order):
            child_sizes = [size[neighbor] for neighbor in graph[node] if parent[neighbor] == node]
            if len(set(child_sizes)) <= 1:
                answer += 1
            if parent[node] != -1:
                size[parent[node]] += size[node]
        return answer
