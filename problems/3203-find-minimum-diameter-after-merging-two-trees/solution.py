# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:30Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def diameter(edges: List[List[int]]) -> int:
            size = len(edges) + 1
            graph = [[] for _ in range(size)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            def farthest(start: int) -> tuple[int, int]:
                queue = deque([(start, -1, 0)])
                far_node, far_dist = start, 0
                while queue:
                    node, parent, dist = queue.popleft()
                    if dist > far_dist:
                        far_node, far_dist = node, dist
                    for neighbor in graph[node]:
                        if neighbor != parent:
                            queue.append((neighbor, node, dist + 1))
                return far_node, far_dist

            endpoint, _ = farthest(0)
            return farthest(endpoint)[1]

        first = diameter(edges1)
        second = diameter(edges2)
        joined = (first + 1) // 2 + (second + 1) // 2 + 1
        return max(first, second, joined)
