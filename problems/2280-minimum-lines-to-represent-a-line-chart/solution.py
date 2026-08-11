# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:23Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) == 1:
            return 0

        points = sorted(stockPrices)
        lines = 1

        for index in range(2, len(points)):
            previous_day_change = points[index - 1][0] - points[index - 2][0]
            previous_price_change = points[index - 1][1] - points[index - 2][1]
            current_day_change = points[index][0] - points[index - 1][0]
            current_price_change = points[index][1] - points[index - 1][1]

            if (
                previous_price_change * current_day_change
                != current_price_change * previous_day_change
            ):
                lines += 1

        return lines
