# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:58Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        import math

        def distance_sum(x, y):
            return sum(math.hypot(x - point_x, y - point_y)
                       for point_x, point_y in positions)

        x = sum(point_x for point_x, _ in positions) / len(positions)
        y = sum(point_y for _, point_y in positions) / len(positions)
        step = 100.0
        answer = distance_sum(x, y)
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while step > 1e-7:
            improved = False
            for delta_x, delta_y in directions:
                next_x = x + delta_x * step
                next_y = y + delta_y * step
                candidate = distance_sum(next_x, next_y)
                if candidate < answer:
                    x, y, answer = next_x, next_y, candidate
                    improved = True
                    break
            if not improved:
                step *= 0.5
        return answer
