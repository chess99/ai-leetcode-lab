# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:20Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        for center_x, center_y, radius in circles:
            radius_squared = radius * radius
            for x in range(center_x - radius, center_x + radius + 1):
                for y in range(center_y - radius, center_y + radius + 1):
                    if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius_squared:
                        points.add((x, y))
        return len(points)
