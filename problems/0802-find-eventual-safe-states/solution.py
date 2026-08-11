# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:46:07Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reverse = [[] for _ in graph]; degree = [len(edges) for edges in graph]
        for node, edges in enumerate(graph):
            for nxt in edges: reverse[nxt].append(node)
        queue = deque(i for i, d in enumerate(degree) if d == 0)
        while queue:
            node = queue.popleft()
            for prev in reverse[node]:
                degree[prev] -= 1
                if degree[prev] == 0: queue.append(prev)
        return [i for i, d in enumerate(degree) if d == 0]
