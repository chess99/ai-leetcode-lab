# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        best_a, best_b = 0, 0
        for energy_a, energy_b in zip(energyDrinkA, energyDrinkB):
            best_a, best_b = max(best_a + energy_a, best_b), max(best_b + energy_b, best_a)
        return max(best_a, best_b)
