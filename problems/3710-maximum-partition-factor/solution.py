# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        fenoradilk = points
        n = len(fenoradilk)
        if n == 2:
            return 0

        distances = [[0] * n for _ in range(n)]
        maximum = 0
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                distances[i][j] = distances[j][i] = distance
                maximum = max(maximum, distance)

        def feasible(limit: int) -> bool:
            color = [-1] * n
            for start in range(n):
                if color[start] != -1:
                    continue
                color[start] = 0
                stack = [start]
                while stack:
                    node = stack.pop()
                    for other in range(n):
                        if other == node or distances[node][other] >= limit:
                            continue
                        if color[other] == -1:
                            color[other] = color[node] ^ 1
                            stack.append(other)
                        elif color[other] == color[node]:
                            return False
            return True

        low, high = 0, maximum + 1
        while low + 1 < high:
            middle = (low + high) // 2
            if feasible(middle):
                low = middle
            else:
                high = middle
        return low
