# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:53:32Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        next_rain = [float("inf")] * len(rains)
        next_day_for_lake = {}
        for day in range(len(rains) - 1, -1, -1):
            lake = rains[day]
            if lake:
                if lake in next_day_for_lake:
                    next_rain[day] = next_day_for_lake[lake]
                next_day_for_lake[lake] = day

        answer = [1] * len(rains)
        full_lakes = set()
        lakes_to_dry = []

        for day, lake in enumerate(rains):
            if lake == 0:
                if lakes_to_dry:
                    _, lake_to_dry = heapq.heappop(lakes_to_dry)
                    full_lakes.remove(lake_to_dry)
                    answer[day] = lake_to_dry
                continue

            if lake in full_lakes:
                return []

            full_lakes.add(lake)
            heapq.heappush(lakes_to_dry, (next_rain[day], lake))
            answer[day] = -1

        return answer
