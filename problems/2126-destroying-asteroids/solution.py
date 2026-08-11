# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        current_mass = mass

        for asteroid in sorted(asteroids):
            if current_mass < asteroid:
                return False
            current_mass += asteroid

        return True
