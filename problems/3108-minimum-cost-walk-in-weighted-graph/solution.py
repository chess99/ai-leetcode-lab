# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parent = list(range(n))

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for first, second, _ in edges:
            first, second = find(first), find(second)
            if first != second:
                parent[first] = second
        component_and = [-1] * n
        for first, _, weight in edges:
            root = find(first)
            component_and[root] &= weight
        answer = []
        for first, second in query:
            if first == second:
                answer.append(0)
            elif find(first) != find(second):
                answer.append(-1)
            else:
                answer.append(component_and[find(first)])
        return answer
