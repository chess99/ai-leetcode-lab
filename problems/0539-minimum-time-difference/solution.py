# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:16:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted(int(point[:2]) * 60 + int(point[3:]) for point in timePoints)
        minimum = min(b - a for a, b in zip(minutes, minutes[1:]))
        return min(minimum, minutes[0] + 24 * 60 - minutes[-1])
