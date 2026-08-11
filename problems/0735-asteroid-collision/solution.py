# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:41:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        survivors = []
        for asteroid in asteroids:
            while survivors and survivors[-1] > 0 > asteroid and survivors[-1] < -asteroid:
                survivors.pop()
            if survivors and survivors[-1] > 0 > asteroid:
                if survivors[-1] == -asteroid:
                    survivors.pop()
                continue
            survivors.append(asteroid)
        return survivors
