# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False
        for value in range(2, int(n ** 0.5) + 1):
            if prime[value]:
                for multiple in range(value * value, n + 1, value):
                    prime[multiple] = False
        graph = [[] for _ in range(n + 1)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
        component = [0] * (n + 1)
        sizes = [0]
        for start in range(1, n + 1):
            if prime[start] or component[start]:
                continue
            identifier = len(sizes)
            stack = [start]
            component[start] = identifier
            size = 0
            while stack:
                node = stack.pop()
                size += 1
                for neighbor in graph[node]:
                    if not prime[neighbor] and not component[neighbor]:
                        component[neighbor] = identifier
                        stack.append(neighbor)
            sizes.append(size)
        answer = 0
        for node in range(1, n + 1):
            if not prime[node]:
                continue
            previous = 0
            for neighbor in graph[node]:
                if prime[neighbor]:
                    continue
                size = sizes[component[neighbor]]
                answer += size + previous * size
                previous += size
        return answer
