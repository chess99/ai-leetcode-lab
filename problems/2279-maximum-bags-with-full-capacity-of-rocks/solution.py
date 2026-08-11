# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:23Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        needed = sorted(
            maximum - current for maximum, current in zip(capacity, rocks)
        )
        full_bags = 0

        for deficit in needed:
            if deficit > additionalRocks:
                break
            additionalRocks -= deficit
            full_bags += 1

        return full_bags
