# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        qoravelin = units
        if len(units[0]) == 1:
            return sum(row[0] for row in units)
        minimum = float('inf')
        seconds = []
        for row in units:
            first, second = sorted(row)[:2]
            minimum = min(minimum, first)
            seconds.append(second)
        return minimum + sum(seconds) - min(seconds)
