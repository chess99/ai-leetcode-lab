# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:58Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]
        for index, (first, second, weight) in enumerate(edges):
            graph[first].append((second, weight, index))
            graph[second].append((first, weight, index))

        def distances(start):
            result = [10 ** 30] * n
            result[start] = 0
            queue = [(0, start)]
            while queue:
                distance, node = heapq.heappop(queue)
                if distance != result[node]:
                    continue
                for neighbor, weight, _ in graph[node]:
                    candidate = distance + weight
                    if candidate < result[neighbor]:
                        result[neighbor] = candidate
                        heapq.heappush(queue, (candidate, neighbor))
            return result

        from_start = distances(0)
        from_end = distances(n - 1)
        shortest = from_start[-1]
        return [(from_start[first] + weight + from_end[second] == shortest
                 or from_start[second] + weight + from_end[first] == shortest)
                for first, second, weight in edges]
