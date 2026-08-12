# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        from collections import deque

        size = len(coins)
        graph = [[] for _ in coins]
        degree = [0] * size
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
            degree[first] += 1
            degree[second] += 1

        remaining_edges = len(edges)
        queue = deque(
            node for node in range(size)
            if degree[node] == 1 and coins[node] == 0
        )
        while queue:
            node = queue.popleft()
            if degree[node] == 0:
                continue
            degree[node] = 0
            remaining_edges -= 1
            for neighbor in graph[node]:
                if degree[neighbor] == 0:
                    continue
                degree[neighbor] -= 1
                if degree[neighbor] == 1 and coins[neighbor] == 0:
                    queue.append(neighbor)
                break

        queue = deque(node for node in range(size) if degree[node] == 1)
        for _ in range(2):
            for _ in range(len(queue)):
                node = queue.popleft()
                if degree[node] == 0:
                    continue
                degree[node] = 0
                remaining_edges -= 1
                for neighbor in graph[node]:
                    if degree[neighbor] == 0:
                        continue
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
                    break

        return max(0, remaining_edges * 2)
