# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:17Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        graph = [[] for _ in range(n)]
        for source, target, weight in edges:
            graph[target].append((source, weight))
        dist = [float('inf')] * n
        dist[0] = 0
        heap = [(0, 0)]
        while heap:
            cost, node = heapq.heappop(heap)
            if cost != dist[node]:
                continue
            for nxt, weight in graph[node]:
                candidate = max(cost, weight)
                if candidate < dist[nxt]:
                    dist[nxt] = candidate
                    heapq.heappush(heap, (candidate, nxt))
        answer = max(dist)
        return -1 if answer == float('inf') else answer
