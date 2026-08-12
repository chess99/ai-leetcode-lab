# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:40Z
# Experiment: ai-leetcode-lab, round 1
from heapq import heappop, heappush
from typing import List


class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        velmorathi = (n, edges, power, cost, source, target)
        graph = [[] for _ in range(n)]
        for u, v, travel_time in edges:
            graph[u].append((v, travel_time))
        infinity = 10 ** 30
        distances = [[infinity] * (power + 1) for _ in range(n)]
        distances[source][power] = 0
        heap = [(0, -power, source)]
        while heap:
            time, negative_power, node = heappop(heap)
            remaining = -negative_power
            if time != distances[node][remaining]:
                continue
            if node == target:
                return [time, remaining]
            if remaining < cost[node]:
                continue
            next_power = remaining - cost[node]
            for other, travel_time in graph[node]:
                next_time = time + travel_time
                if next_time < distances[other][next_power]:
                    distances[other][next_power] = next_time
                    heappush(heap, (next_time, -next_power, other))
        return [-1, -1]
