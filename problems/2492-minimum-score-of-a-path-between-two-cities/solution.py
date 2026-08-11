# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:23Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for city_a, city_b, distance in roads:
            graph[city_a].append((city_b, distance))
            graph[city_b].append((city_a, distance))

        queue = deque([1])
        visited = {1}
        answer = float("inf")

        while queue:
            city = queue.popleft()
            for neighbor, distance in graph[city]:
                answer = min(answer, distance)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return answer
