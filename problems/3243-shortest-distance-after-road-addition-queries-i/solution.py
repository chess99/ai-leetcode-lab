# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        from collections import deque

        graph = [[node + 1] for node in range(n - 1)] + [[]]
        answer = []
        for start, end in queries:
            graph[start].append(end)
            distance = [-1] * n
            distance[0] = 0
            queue = deque([0])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if distance[neighbor] == -1:
                        distance[neighbor] = distance[node] + 1
                        queue.append(neighbor)
            answer.append(distance[-1])
        return answer
