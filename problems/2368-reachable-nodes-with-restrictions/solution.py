# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        blocked = set(restricted)
        visited = {0}
        stack = [0]

        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor in blocked or neighbor in visited:
                    continue
                visited.add(neighbor)
                stack.append(neighbor)

        return len(visited)
