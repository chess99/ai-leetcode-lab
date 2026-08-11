# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:27Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 0, min(ranks) * cars * cars
        while left < right:
            time = (left + right) // 2
            repaired = sum(int((time // rank) ** 0.5) for rank in ranks)
            if repaired >= cars:
                right = time
            else:
                left = time + 1
        return left
