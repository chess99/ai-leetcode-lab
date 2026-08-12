# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        graph = [[] for _ in cost]
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

        answer = [1] * n
        summaries = [None] * n
        subtree_size = [1] * n
        for node in reversed(order):
            values = [cost[node]]
            for neighbor in graph[node]:
                if parent[neighbor] == node:
                    subtree_size[node] += subtree_size[neighbor]
                    values.extend(summaries[neighbor])
            values.sort()
            if subtree_size[node] >= 3:
                answer[node] = max(0,
                                   values[-1] * values[-2] * values[-3],
                                   values[0] * values[1] * values[-1])
            summaries[node] = values if len(values) <= 5 else values[:2] + values[-3:]
        return answer
