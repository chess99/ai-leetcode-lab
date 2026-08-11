# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:23:16Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[[] for _ in range(n)] for _ in range(2)]
        for color, edges in enumerate((redEdges, blueEdges)):
            for start, end in edges:
                graph[color][start].append(end)
        answer = [-1] * n
        queue = deque([(0, 0), (0, 1)])
        visited = set(queue)
        distance = 0
        while queue:
            for _ in range(len(queue)):
                node, color = queue.popleft()
                if answer[node] == -1:
                    answer[node] = distance
                for neighbor in graph[color][node]:
                    state = (neighbor, 1 - color)
                    if state not in visited:
                        visited.add(state)
                        queue.append(state)
            distance += 1
        return answer
