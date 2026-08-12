# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)
        for start in range(len(graph)):
            if colors[start]:
                continue
            colors[start] = 1
            stack = [start]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if colors[neighbor] == colors[node]:
                        return False
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[node]
                        stack.append(neighbor)
        return True
