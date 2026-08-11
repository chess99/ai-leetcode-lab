# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:21:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        difference = [0] * (n + 1)
        for first, last, seats in bookings:
            difference[first - 1] += seats
            difference[last] -= seats
        for index in range(1, n):
            difference[index] += difference[index - 1]
        return difference[:n]
