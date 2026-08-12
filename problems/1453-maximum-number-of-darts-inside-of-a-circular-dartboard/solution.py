# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:55Z
# Experiment: ai-leetcode-lab, round 1
from math import hypot, sqrt
from typing import List


class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        answer = 1
        radius_squared = r * r
        for index, (first_x, first_y) in enumerate(darts):
            for second_x, second_y in darts[index + 1:]:
                delta_x, delta_y = second_x - first_x, second_y - first_y
                distance = hypot(delta_x, delta_y)
                if distance <= 1e-12:
                    count = sum((x - first_x) ** 2 + (y - first_y) ** 2
                                <= radius_squared + 1e-7 for x, y in darts)
                    answer = max(answer, count)
                    continue
                if distance > 2 * r + 1e-10:
                    continue
                middle_x = (first_x + second_x) / 2
                middle_y = (first_y + second_y) / 2
                offset = sqrt(max(0.0, radius_squared - distance * distance / 4))
                perpendicular_x, perpendicular_y = -delta_y / distance, delta_x / distance
                for sign in (-1, 1):
                    center_x = middle_x + sign * offset * perpendicular_x
                    center_y = middle_y + sign * offset * perpendicular_y
                    count = sum((x - center_x) ** 2 + (y - center_y) ** 2
                                <= radius_squared + 1e-7 for x, y in darts)
                    answer = max(answer, count)
        return answer
