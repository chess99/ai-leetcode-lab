# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        adjacency = [[] for _ in range(n)]
        for source, destination in graph:
            adjacency[source].append(destination)
        stack = [start]
        visited = {start}
        while stack:
            node = stack.pop()
            if node == target:
                return True
            for neighbor in adjacency[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        return False
