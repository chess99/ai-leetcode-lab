# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:48Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        size = len(colors)
        graph = [[] for _ in range(size)]
        indegree = [0] * size
        for first, second in edges:
            graph[first].append(second)
            indegree[second] += 1
        counts = [[0] * 26 for _ in range(size)]
        queue = deque(index for index, degree in enumerate(indegree) if degree == 0)
        processed = answer = 0
        while queue:
            node = queue.popleft()
            processed += 1
            color = ord(colors[node]) - ord('a')
            counts[node][color] += 1
            answer = max(answer, counts[node][color])
            for neighbor in graph[node]:
                for current_color in range(26):
                    counts[neighbor][current_color] = max(
                        counts[neighbor][current_color], counts[node][current_color])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return answer if processed == size else -1
