# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        x1, y1 = start1
        x2, y2 = end1
        x3, y3 = start2
        x4, y4 = end2
        dx1, dy1 = x2 - x1, y2 - y1
        dx2, dy2 = x4 - x3, y4 - y3
        denominator = dx1 * dy2 - dy1 * dx2

        def cross(ax: int, ay: int, bx: int, by: int) -> int:
            return ax * by - ay * bx

        if denominator:
            t_numerator = cross(x3 - x1, y3 - y1, dx2, dy2)
            u_numerator = cross(x3 - x1, y3 - y1, dx1, dy1)
            if denominator < 0:
                denominator = -denominator
                t_numerator = -t_numerator
                u_numerator = -u_numerator
            if 0 <= t_numerator <= denominator and 0 <= u_numerator <= denominator:
                ratio = t_numerator / denominator
                return [x1 + dx1 * ratio, y1 + dy1 * ratio]
            return []

        if cross(x3 - x1, y3 - y1, dx1, dy1):
            return []
        candidates = []
        for point in (start1, end1, start2, end2):
            x, y = point
            if (
                min(x1, x2) <= x <= max(x1, x2)
                and min(y1, y2) <= y <= max(y1, y2)
                and min(x3, x4) <= x <= max(x3, x4)
                and min(y3, y4) <= y <= max(y3, y4)
            ):
                candidates.append(point)
        return list(map(float, min(candidates))) if candidates else []
