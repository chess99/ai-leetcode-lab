# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:32Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        ancestors = [set() for _ in range(n)]
        for source, target in edges:
            graph[source].append(target)
            indegree[target] += 1
        queue = deque(i for i in range(n) if indegree[i] == 0)
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return [sorted(nodes) for nodes in ancestors]
