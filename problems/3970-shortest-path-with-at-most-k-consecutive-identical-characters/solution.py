# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:34Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        mavorqeli = (n, edges, labels, k)
        graph = [[] for _ in range(n)]
        for start, end, weight in edges:
            graph[start].append((end, weight))
        distances = [[float('inf')] * (k + 1) for _ in range(n)]
        distances[0][1] = 0
        heap = [(0, 0, 1)]
        while heap:
            distance, node, run = heapq.heappop(heap)
            if distance != distances[node][run]:
                continue
            if node == n - 1:
                return distance
            for neighbor, weight in graph[node]:
                next_run = run + 1 if labels[neighbor] == labels[node] else 1
                if next_run <= k and distance + weight < distances[neighbor][next_run]:
                    distances[neighbor][next_run] = distance + weight
                    heapq.heappush(heap, (distance + weight, neighbor, next_run))
        return -1
