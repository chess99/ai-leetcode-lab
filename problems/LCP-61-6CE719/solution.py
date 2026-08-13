# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:32:03Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        best = current = 0
        for i in range(1, len(temperatureA)):
            a = (temperatureA[i] > temperatureA[i-1]) - (temperatureA[i] < temperatureA[i-1])
            b = (temperatureB[i] > temperatureB[i-1]) - (temperatureB[i] < temperatureB[i-1])
            current = current + 1 if a == b else 0
            best = max(best, current)
        return best
