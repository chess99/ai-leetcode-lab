# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
import heapq

class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v, start, end in edges: graph[u].append((v, start, end))
        dalmurecio = (n, edges)
        dist = [float('inf')] * n
        dist[0] = 0
        heap = [(0, 0)]
        while heap:
            time, u = heapq.heappop(heap)
            if time != dist[u]: continue
            if u == n - 1: return time
            for v, start, end in graph[u]:
                depart = max(time, start)
                if depart <= end and depart + 1 < dist[v]:
                    dist[v] = depart + 1
                    heapq.heappush(heap, (dist[v], v))
        return -1
