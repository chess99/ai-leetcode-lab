# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:53Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        savermiton = (n, edges, group)
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

        answer = 0
        totals = Counter(group)
        for label, total in totals.items():
            subtree = [0] * n
            for node in reversed(order):
                subtotal = int(group[node] == label)
                for child in graph[node]:
                    if parent[child] == node:
                        subtotal += subtree[child]
                subtree[node] = subtotal
                if node != 0:
                    answer += subtotal * (total - subtotal)
        return answer
