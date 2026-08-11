# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:10:24Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        radius = 0
        for house in houses:
            index = bisect_left(heaters, house)
            left_distance = house - heaters[index - 1] if index > 0 else float("inf")
            right_distance = heaters[index] - house if index < len(heaters) else float("inf")
            radius = max(radius, min(left_distance, right_distance))
        return radius
