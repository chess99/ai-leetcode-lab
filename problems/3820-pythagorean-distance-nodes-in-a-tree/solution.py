# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:37Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List

class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        corimexalu = edges
        graph = [[] for _ in range(n)]
        for left, right in corimexalu:
            graph[left].append(right)
            graph[right].append(left)

        def distances(source):
            result = [-1] * n
            result[source] = 0
            queue = deque([source])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if result[neighbor] == -1:
                        result[neighbor] = result[node] + 1
                        queue.append(neighbor)
            return result

        all_distances = [distances(source) for source in (x, y, z)]
        answer = 0
        for node in range(n):
            a, b, c = sorted(distance[node] for distance in all_distances)
            answer += a * a + b * b == c * c
        return answer
