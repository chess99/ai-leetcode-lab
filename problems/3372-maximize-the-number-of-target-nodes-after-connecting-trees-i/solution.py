# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:16Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def build(edges: List[List[int]]) -> List[List[int]]:
            graph = [[] for _ in range(len(edges) + 1)]
            for a, b in edges:
                graph[a].append(b)
                graph[b].append(a)
            return graph

        def count_within(graph: List[List[int]], start: int, limit: int) -> int:
            queue = deque([(start, 0)])
            seen = {start}
            count = 0
            while queue:
                node, distance = queue.popleft()
                count += 1
                if distance == limit:
                    continue
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append((nei, distance + 1))
            return count

        first, second = build(edges1), build(edges2)
        extra = max(count_within(second, node, k - 1) for node in range(len(second))) if k else 0
        return [count_within(first, node, k) + extra for node in range(len(first))]
