# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:08Z
# Experiment: ai-leetcode-lab, round 1
import sys
from typing import List


class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        sys.setrecursionlimit(50_000)
        graph = [[] for _ in values]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def keep(node: int, parent: int) -> int:
            children = [keep(child, node) for child in graph[node] if child != parent]
            if not children:
                return values[node]
            return min(values[node], sum(children))

        return sum(values) - keep(0, -1)
