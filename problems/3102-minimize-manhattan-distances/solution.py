# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        first = sorted((x + y, index) for index, (x, y) in enumerate(points))
        second = sorted((x - y, index) for index, (x, y) in enumerate(points))

        def remaining_range(values, removed):
            low = values[1][0] if values[0][1] == removed else values[0][0]
            high = values[-2][0] if values[-1][1] == removed else values[-1][0]
            return high - low

        return min(max(remaining_range(first, index), remaining_range(second, index))
                   for index in range(len(points)))
