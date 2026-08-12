# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:42Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph = [[] for _ in range(n)]
        reverse = [[] for _ in range(n)]
        for start, end, weight in edges:
            graph[start].append((end, weight))
            reverse[end].append((start, weight))

        def dijkstra(start, adjacency):
            distances = [float("inf")] * n
            distances[start] = 0
            queue = [(0, start)]
            while queue:
                distance, node = heapq.heappop(queue)
                if distance != distances[node]:
                    continue
                for neighbor, weight in adjacency[node]:
                    candidate = distance + weight
                    if candidate < distances[neighbor]:
                        distances[neighbor] = candidate
                        heapq.heappush(queue, (candidate, neighbor))
            return distances

        from_first = dijkstra(src1, graph)
        from_second = dijkstra(src2, graph)
        to_destination = dijkstra(dest, reverse)
        answer = min(
            from_first[node] + from_second[node] + to_destination[node]
            for node in range(n)
        )
        return -1 if answer == float("inf") else answer
