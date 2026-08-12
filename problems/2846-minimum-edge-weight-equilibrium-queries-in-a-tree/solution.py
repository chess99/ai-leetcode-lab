# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for first, second, weight in edges:
            graph[first].append((second, weight))
            graph[second].append((first, weight))
        levels = max(1, n.bit_length())
        parent = [[-1] * n for _ in range(levels)]
        depth = [0] * n
        counts = [[0] * 27 for _ in range(n)]
        stack = [0]
        order = [0]
        while stack:
            node = stack.pop()
            for neighbor, weight in graph[node]:
                if neighbor == parent[0][node]:
                    continue
                parent[0][neighbor] = node
                depth[neighbor] = depth[node] + 1
                counts[neighbor] = counts[node][:]
                counts[neighbor][weight] += 1
                stack.append(neighbor)
                order.append(neighbor)
        for level in range(1, levels):
            for node in range(n):
                ancestor = parent[level - 1][node]
                parent[level][node] = (-1 if ancestor == -1
                                       else parent[level - 1][ancestor])

        def lca(first, second):
            if depth[first] < depth[second]:
                first, second = second, first
            difference = depth[first] - depth[second]
            for bit in range(levels):
                if difference >> bit & 1:
                    first = parent[bit][first]
            if first == second:
                return first
            for bit in range(levels - 1, -1, -1):
                if parent[bit][first] != parent[bit][second]:
                    first = parent[bit][first]
                    second = parent[bit][second]
            return parent[0][first]

        answer = []
        for first, second in queries:
            ancestor = lca(first, second)
            length = depth[first] + depth[second] - 2 * depth[ancestor]
            most = max(counts[first][weight] + counts[second][weight]
                       - 2 * counts[ancestor][weight]
                       for weight in range(1, 27))
            answer.append(length - most)
        return answer
