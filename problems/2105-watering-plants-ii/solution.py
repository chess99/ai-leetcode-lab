# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        left, right = 0, len(plants) - 1
        water_a, water_b = capacityA, capacityB
        refills = 0

        while left < right:
            if water_a < plants[left]:
                refills += 1
                water_a = capacityA
            water_a -= plants[left]
            left += 1

            if water_b < plants[right]:
                refills += 1
                water_b = capacityB
            water_b -= plants[right]
            right -= 1

        if left == right:
            needed = plants[left]
            if max(water_a, water_b) < needed:
                refills += 1

        return refills
