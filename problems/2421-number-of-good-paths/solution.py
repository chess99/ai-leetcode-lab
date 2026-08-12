# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:53Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        size = len(vals)
        graph = [[] for _ in range(size)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
        parent = list(range(size))

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        groups = {}
        for node, value in enumerate(vals):
            groups.setdefault(value, []).append(node)
        answer = size
        active = [False] * size
        for value in sorted(groups):
            for node in groups[value]:
                active[node] = True
                for neighbor in graph[node]:
                    if active[neighbor]:
                        first = find(node)
                        second = find(neighbor)
                        if first != second:
                            parent[first] = second
            counts = Counter(find(node) for node in groups[value])
            answer += sum(count * (count - 1) // 2 for count in counts.values())
        return answer
