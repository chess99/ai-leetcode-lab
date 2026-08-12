# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:29:01Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxActivated(self, points: list[list[int]]) -> int:
        relqavindo = points
        n = len(points)
        parent = list(range(n))
        size = [1] * n

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(a, b):
            a, b = find(a), find(b)
            if a == b:
                return
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]

        by_x = {}
        by_y = {}
        for index, (x, y) in enumerate(points):
            if x in by_x:
                union(index, by_x[x])
            else:
                by_x[x] = index
            if y in by_y:
                union(index, by_y[y])
            else:
                by_y[y] = index

        component_size = {}
        for index in range(n):
            root = find(index)
            component_size[root] = component_size.get(root, 0) + 1
        largest = sorted(component_size.values(), reverse=True)
        return 1 + largest[0] + (largest[1] if len(largest) > 1 else 0)
