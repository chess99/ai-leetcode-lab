# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = [set() for _ in range(n + 1)]
        for first, second in edges:
            graph[first].add(second)
            graph[second].add(first)
        odd = [node for node in range(1, n + 1) if len(graph[node]) % 2]
        if not odd:
            return True
        if len(odd) == 2:
            first, second = odd
            if second not in graph[first]:
                return True
            return any(
                node not in graph[first] and node not in graph[second]
                for node in range(1, n + 1)
                if node != first and node != second
            )
        if len(odd) == 4:
            first, second, third, fourth = odd
            return any(
                b not in graph[a] and d not in graph[c]
                for (a, b, c, d) in (
                    (first, second, third, fourth),
                    (first, third, second, fourth),
                    (first, fourth, second, third),
                )
            )
        return False
