# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minRecSize(self, lines: List[List[int]]) -> float:
        by_slope = {}
        for slope, intercept in lines:
            if slope not in by_slope:
                by_slope[slope] = [intercept, intercept]
            else:
                by_slope[slope][0] = min(by_slope[slope][0], intercept)
                by_slope[slope][1] = max(by_slope[slope][1], intercept)

        groups = sorted(by_slope.items())
        if len(groups) < 2:
            return 0.0
        min_x = min_y = float("inf")
        max_x = max_y = float("-inf")
        for index in range(len(groups) - 1):
            k1, bounds1 = groups[index]
            k2, bounds2 = groups[index + 1]
            for b1 in bounds1:
                for b2 in bounds2:
                    x = (b1 - b2) / (k2 - k1)
                    y = (k2 * b1 - k1 * b2) / (k2 - k1)
                    min_x = min(min_x, x)
                    max_x = max(max_x, x)
                    min_y = min(min_y, y)
                    max_y = max(max_y, y)
        return (max_x - min_x) * (max_y - min_y)
