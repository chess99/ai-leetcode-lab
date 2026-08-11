# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:41:41Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for source, target, weight in times:
            graph[source].append((target, weight))
        distances = {k: 0}
        heap = [(0, k)]
        while heap:
            distance, node = heappop(heap)
            if distance != distances[node]:
                continue
            for neighbor, weight in graph[node]:
                candidate = distance + weight
                if candidate < distances.get(neighbor, float("inf")):
                    distances[neighbor] = candidate
                    heappush(heap, (candidate, neighbor))
        return max(distances.values()) if len(distances) == n else -1
