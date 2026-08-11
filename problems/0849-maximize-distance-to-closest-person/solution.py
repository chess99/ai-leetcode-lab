# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:50:04Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        previous = -1
        best = 0
        for index, seat in enumerate(seats):
            if seat:
                best = max(best, index if previous == -1 else (index - previous) // 2)
                previous = index
        return max(best, len(seats) - 1 - previous)
