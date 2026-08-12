# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        size = len(coins)
        graph = [[] for _ in range(size)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
        parent = [-1] * size
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)
        levels = 15
        dynamic = [[0] * levels for _ in range(size)]
        for node in reversed(order):
            for shift in range(levels):
                first = (coins[node] >> shift) - k
                second = coins[node] >> (shift + 1)
                for neighbor in graph[node]:
                    if parent[neighbor] == node:
                        first += dynamic[neighbor][shift]
                        second += dynamic[neighbor][min(levels - 1, shift + 1)]
                dynamic[node][shift] = max(first, second)
        return dynamic[0][0]
