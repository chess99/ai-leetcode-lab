# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        from math import gcd
        best = 0
        for i, (x1, y1) in enumerate(points):
            slopes = {}; duplicates = 1
            for x2, y2 in points[i + 1:]:
                dx, dy = x2 - x1, y2 - y1
                if not dx and not dy: duplicates += 1; continue
                g = gcd(dx, dy); dx //= g; dy //= g
                if dx < 0: dx, dy = -dx, -dy
                if dx == 0: dy = 1
                if dy == 0: dx = 1
                slopes[(dx, dy)] = slopes.get((dx, dy), 0) + 1
            best = max(best, duplicates + max(slopes.values(), default=0))
        return best
