# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:43Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        threnquivar = edges
        graph = [[] for _ in range(n)]
        for source, target, cost in threnquivar:
            graph[source].append((target, cost))
            graph[target].append((source, cost * 2))
        distance = [float('inf')] * n
        distance[0] = 0
        heap = [(0, 0)]
        while heap:
            cost, node = heapq.heappop(heap)
            if cost != distance[node]:
                continue
            if node == n - 1:
                return cost
            for target, edge_cost in graph[node]:
                new_cost = cost + edge_cost
                if new_cost < distance[target]:
                    distance[target] = new_cost
                    heapq.heappush(heap, (new_cost, target))
        return -1
