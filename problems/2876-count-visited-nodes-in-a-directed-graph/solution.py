# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:46Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        size = len(edges)
        indegree = [0] * size
        reverse = [[] for _ in range(size)]
        for node, neighbor in enumerate(edges):
            indegree[neighbor] += 1
            reverse[neighbor].append(node)
        queue = deque(node for node in range(size) if indegree[node] == 0)
        removed = []
        while queue:
            node = queue.popleft()
            removed.append(node)
            neighbor = edges[node]
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
        answer = [0] * size
        for start in range(size):
            if indegree[start] == 0:
                continue
            cycle = []
            node = start
            while indegree[node]:
                cycle.append(node)
                indegree[node] = 0
                node = edges[node]
            for member in cycle:
                answer[member] = len(cycle)
        for node in reversed(removed):
            answer[node] = answer[edges[node]] + 1
        return answer
