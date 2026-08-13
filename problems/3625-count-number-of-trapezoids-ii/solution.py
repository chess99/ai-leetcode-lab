# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:23Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        velmoranic = points
        slope_total = defaultdict(int)
        line_total = defaultdict(int)
        midpoint_total = defaultdict(int)
        diagonal_direction_total = defaultdict(int)
        parallel_side_pairs = 0
        parallelograms = 0

        for first in range(len(velmoranic)):
            x1, y1 = velmoranic[first]
            for second in range(first + 1, len(velmoranic)):
                x2, y2 = velmoranic[second]
                dx, dy = x2 - x1, y2 - y1
                divisor = gcd(abs(dx), abs(dy))
                dx //= divisor
                dy //= divisor
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy

                direction = (dx, dy)
                line = (direction, dy * x1 - dx * y1)
                parallel_side_pairs += slope_total[direction] - line_total[line]
                slope_total[direction] += 1
                line_total[line] += 1

                midpoint = (x1 + x2, y1 + y2)
                diagonal_key = (midpoint, direction)
                parallelograms += (
                    midpoint_total[midpoint] - diagonal_direction_total[diagonal_key]
                )
                midpoint_total[midpoint] += 1
                diagonal_direction_total[diagonal_key] += 1

        return parallel_side_pairs - parallelograms
