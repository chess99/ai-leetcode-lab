# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:27Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (numerator, denominator), value in zip(equations, values):
            graph[numerator].append((denominator, value))
            graph[denominator].append((numerator, 1.0 / value))

        def evaluate(start: str, target: str) -> float:
            if start not in graph or target not in graph:
                return -1.0
            stack = [(start, 1.0)]
            visited = {start}
            while stack:
                node, product = stack.pop()
                if node == target:
                    return product
                for neighbor, ratio in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append((neighbor, product * ratio))
            return -1.0

        return [evaluate(start, target) for start, target in queries]
