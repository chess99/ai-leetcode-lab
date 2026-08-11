# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:52:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for source, target in connections:
            graph[source].append((target, 1))
            graph[target].append((source, 0))
        changes = 0
        seen = {0}
        stack = [0]
        while stack:
            city = stack.pop()
            for neighbor, needs_change in graph[city]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    changes += needs_change
                    stack.append(neighbor)
        return changes
