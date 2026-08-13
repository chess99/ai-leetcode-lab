# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:01:01Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def cutSquares(self, square1: List[int], square2: List[int]) -> List[float]:
        x1, y1, side1 = square1
        x2, y2, side2 = square2
        center1 = (x1 + side1 / 2, y1 + side1 / 2)
        center2 = (x2 + side2 / 2, y2 + side2 / 2)
        if center1[0] == center2[0]:
            low = min(y1, y2)
            high = max(y1 + side1, y2 + side2)
            return [center1[0], low, center1[0], high]
        slope = (center2[1] - center1[1]) / (center2[0] - center1[0])
        if -1 <= slope <= 1:
            left = min(x1, x2)
            right = max(x1 + side1, x2 + side2)
            intercept = center1[1] - slope * center1[0]
            return [left, slope * left + intercept, right, slope * right + intercept]
        low = min(y1, y2)
        high = max(y1 + side1, y2 + side2)
        inverse_slope = 1 / slope
        intercept = center1[0] - inverse_slope * center1[1]
        first = [inverse_slope * low + intercept, low]
        second = [inverse_slope * high + intercept, high]
        if first[0] > second[0]:
            first, second = second, first
        return first + second
