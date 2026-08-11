# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:14:58Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        point_count = len(points)
        minimum_cost = [float("inf")] * point_count
        minimum_cost[0] = 0
        included = [False] * point_count
        total_cost = 0

        for _ in range(point_count):
            current = -1
            for point in range(point_count):
                if not included[point] and (
                    current == -1 or minimum_cost[point] < minimum_cost[current]
                ):
                    current = point

            included[current] = True
            total_cost += minimum_cost[current]
            x1, y1 = points[current]

            for neighbor, (x2, y2) in enumerate(points):
                if not included[neighbor]:
                    distance = abs(x1 - x2) + abs(y1 - y2)
                    minimum_cost[neighbor] = min(minimum_cost[neighbor], distance)

        return total_cost
