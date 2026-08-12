# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
        count = len(circles)
        side_a, side_b = count, count + 1
        parent = list(range(count + 2))

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(first: int, second: int) -> None:
            first, second = find(first), find(second)
            if first != second:
                parent[first] = second

        def touches_vertical(x: int, y: int, radius: int, line_x: int) -> bool:
            dx = abs(x - line_x)
            dy = max(0, y - yCorner)
            return dx * dx + dy * dy <= radius * radius

        def touches_horizontal(x: int, y: int, radius: int, line_y: int) -> bool:
            dx = max(0, x - xCorner)
            dy = abs(y - line_y)
            return dx * dx + dy * dy <= radius * radius

        for i, (x, y, radius) in enumerate(circles):
            if touches_vertical(x, y, radius, 0) or touches_horizontal(x, y, radius, yCorner):
                union(i, side_a)
            if touches_horizontal(x, y, radius, 0) or touches_vertical(x, y, radius, xCorner):
                union(i, side_b)

            for j in range(i):
                other_x, other_y, other_radius = circles[j]
                radius_sum = radius + other_radius
                if (x - other_x) ** 2 + (y - other_y) ** 2 > radius_sum**2:
                    continue

                # 两圆内部的这个加权分点同时属于两圆；仅当它位于矩形内时，
                # 两个障碍在可行区域中才需要视为连通。
                weighted_x = x * other_radius + other_x * radius
                weighted_y = y * other_radius + other_y * radius
                if weighted_x < radius_sum * xCorner and weighted_y < radius_sum * yCorner:
                    union(i, j)

            if find(side_a) == find(side_b):
                return False

        return True
