# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:29Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for first, second in edges:
            first -= 1
            second -= 1
            graph[first].append(second)
            graph[second].append(first)

        color = [-1] * n
        components = []
        for start in range(n):
            if color[start] != -1:
                continue
            color[start] = 0
            queue = deque([start])
            component = []
            while queue:
                node = queue.popleft()
                component.append(node)
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = color[node] ^ 1
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return -1
            components.append(component)

        answer = 0
        for component in components:
            maximum_layers = 0
            for start in component:
                distances = {start: 0}
                queue = deque([start])
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor not in distances:
                            distances[neighbor] = distances[node] + 1
                            queue.append(neighbor)
                maximum_layers = max(maximum_layers, max(distances.values()) + 1)
            answer += maximum_layers
        return answer
