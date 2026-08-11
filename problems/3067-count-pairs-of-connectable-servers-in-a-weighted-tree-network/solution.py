# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for left, right, weight in edges:
            graph[left].append((right, weight))
            graph[right].append((left, weight))

        def count_divisible(node: int, parent: int, distance: int) -> int:
            total = 0
            stack = [(node, parent, distance)]
            while stack:
                current, previous, current_distance = stack.pop()
                total += current_distance % signalSpeed == 0
                for neighbor, weight in graph[current]:
                    if neighbor != previous:
                        stack.append((neighbor, current, current_distance + weight))
            return total

        answer = []
        for center in range(n):
            seen, pairs = 0, 0
            for neighbor, weight in graph[center]:
                count = count_divisible(neighbor, center, weight)
                pairs += seen * count
                seen += count
            answer.append(pairs)
        return answer
