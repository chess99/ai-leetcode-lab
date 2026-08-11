# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, min(time) * totalTrips
        while left < right:
            middle = (left + right) // 2
            if sum(middle // trip_time for trip_time in time) >= totalTrips:
                right = middle
            else:
                left = middle + 1
        return left
