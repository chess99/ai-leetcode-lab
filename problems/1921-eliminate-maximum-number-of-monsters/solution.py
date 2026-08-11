# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:05Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrivals = sorted((distance - 1) // velocity for distance, velocity in zip(dist, speed))
        for minute, arrival in enumerate(arrivals):
            if arrival < minute: return minute
        return len(dist)
