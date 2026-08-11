# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:24Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        count = len(bombs)
        graph = [[] for _ in range(count)]

        for source, (x1, y1, radius) in enumerate(bombs):
            for target, (x2, y2, _) in enumerate(bombs):
                distance_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if distance_squared <= radius**2:
                    graph[source].append(target)

        best = 0
        for start in range(count):
            seen = {start}
            stack = [start]
            while stack:
                source = stack.pop()
                for target in graph[source]:
                    if target not in seen:
                        seen.add(target)
                        stack.append(target)
            best = max(best, len(seen))

        return best
