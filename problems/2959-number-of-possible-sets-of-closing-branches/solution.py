# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        infinity = 10 ** 15
        answer = 0
        for mask in range(1 << n):
            distance = [[infinity] * n for _ in range(n)]
            for node in range(n):
                if mask >> node & 1:
                    distance[node][node] = 0
            for first, second, weight in roads:
                if mask >> first & 1 and mask >> second & 1:
                    distance[first][second] = min(distance[first][second], weight)
                    distance[second][first] = min(distance[second][first], weight)
            for middle in range(n):
                if not (mask >> middle & 1):
                    continue
                for first in range(n):
                    for second in range(n):
                        distance[first][second] = min(
                            distance[first][second],
                            distance[first][middle] + distance[middle][second],
                        )
            nodes = [node for node in range(n) if mask >> node & 1]
            if all(distance[first][second] <= maxDistance
                   for first in nodes for second in nodes):
                answer += 1
        return answer
