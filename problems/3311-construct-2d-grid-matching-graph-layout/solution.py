# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:34Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [set() for _ in range(n)]
        for first, second in edges:
            graph[first].add(second)
            graph[second].add(first)

        if any(len(neighbors) == 1 for neighbors in graph):
            start = next(node for node in range(n) if len(graph[node]) == 1)
            row = []
            previous = -1
            current = start
            while current != -1:
                row.append(current)
                following = [neighbor for neighbor in graph[current]
                             if neighbor != previous]
                previous, current = current, (following[0] if following else -1)
            return [row]

        corner = next(node for node in range(n) if len(graph[node]) == 2)
        first_row = [corner]
        previous = -1
        current = corner
        while len(first_row) == 1 or len(graph[current]) != 2:
            following = [neighbor for neighbor in graph[current]
                         if neighbor != previous and len(graph[neighbor]) < 4]
            following.sort(key=lambda node: len(graph[node]))
            next_node = following[0]
            first_row.append(next_node)
            previous, current = current, next_node

        layout = [first_row]
        used = set(first_row)
        while len(used) < n:
            row = []
            for above in layout[-1]:
                candidate = next(neighbor for neighbor in graph[above]
                                 if neighbor not in used
                                 and (not row or neighbor in graph[row[-1]]))
                row.append(candidate)
                used.add(candidate)
            layout.append(row)
        return layout
