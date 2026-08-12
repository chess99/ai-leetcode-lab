# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:52Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = [[] for _ in range(n + 1)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
        queue = deque([(1, 0, 1.0, 0)])
        while queue:
            node, parent, probability, elapsed = queue.popleft()
            children = [neighbor for neighbor in graph[node] if neighbor != parent]
            if node == target:
                return probability if elapsed == t or not children else 0.0
            if elapsed == t or not children:
                continue
            share = probability / len(children)
            for child in children:
                queue.append((child, node, share, elapsed + 1))
        return 0.0
