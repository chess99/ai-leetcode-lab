# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:47Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def electricCarPlan(self, paths: List[List[int]], cnt: int, start: int, end: int, charge: List[int]) -> int:
        city_count = len(charge)
        graph = [[] for _ in range(city_count)]
        for left, right, distance in paths:
            graph[left].append((right, distance))
            graph[right].append((left, distance))

        infinity = 10**30
        best = [[infinity] * (cnt + 1) for _ in range(city_count)]
        best[start][0] = 0
        heap = [(0, start, 0)]
        while heap:
            elapsed, city, battery = heapq.heappop(heap)
            if elapsed != best[city][battery]:
                continue
            if city == end:
                return elapsed
            if battery < cnt:
                next_elapsed = elapsed + charge[city]
                if next_elapsed < best[city][battery + 1]:
                    best[city][battery + 1] = next_elapsed
                    heapq.heappush(heap, (next_elapsed, city, battery + 1))
            for neighbor, consumption in graph[city]:
                if consumption <= battery:
                    next_elapsed = elapsed + consumption
                    next_battery = battery - consumption
                    if next_elapsed < best[neighbor][next_battery]:
                        best[neighbor][next_battery] = next_elapsed
                        heapq.heappush(heap, (next_elapsed, neighbor, next_battery))
        return -1
