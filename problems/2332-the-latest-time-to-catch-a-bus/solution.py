# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:27Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def latestTimeCatchTheBus(
        self, buses: List[int], passengers: List[int], capacity: int
    ) -> int:
        buses.sort()
        passengers.sort()
        passenger_index = 0
        boarded_last = 0

        for bus in buses:
            boarded = 0
            while (
                boarded < capacity
                and passenger_index < len(passengers)
                and passengers[passenger_index] <= bus
            ):
                passenger_index += 1
                boarded += 1
            boarded_last = boarded

        if boarded_last < capacity:
            candidate = buses[-1]
        else:
            candidate = passengers[passenger_index - 1] - 1

        passenger_times = set(passengers)
        while candidate in passenger_times:
            candidate -= 1
        return candidate
