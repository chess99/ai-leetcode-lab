# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:21Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        water = capacity

        for index, needed in enumerate(plants):
            if water < needed:
                steps += 2 * index
                water = capacity

            steps += 1
            water -= needed

        return steps
