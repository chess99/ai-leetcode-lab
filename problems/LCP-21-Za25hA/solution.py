# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:45Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def chaseGame(self, edges: List[List[int]], startA: int, startB: int) -> int:
        n = len(edges)
        graph = [[] for _ in range(n + 1)]
        degree = [0] * (n + 1)
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)
            degree[left] += 1
            degree[right] += 1

        def distances(start: int) -> List[int]:
            result = [-1] * (n + 1)
            result[start] = 0
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if result[neighbor] == -1:
                        result[neighbor] = result[node] + 1
                        queue.append(neighbor)
            return result

        dist_a = distances(startA)
        if dist_a[startB] == 1:
            return 1
        dist_b = distances(startB)

        queue = deque(node for node in range(1, n + 1) if degree[node] == 1)
        on_cycle = [True] * (n + 1)
        while queue:
            node = queue.popleft()
            on_cycle[node] = False
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    queue.append(neighbor)

        cycle_size = sum(on_cycle[1:])
        answer = 1
        for node in range(1, n + 1):
            if dist_a[node] > dist_b[node] + 1:
                if cycle_size > 3 and on_cycle[node]:
                    return -1
                answer = max(answer, dist_a[node])
        return answer
