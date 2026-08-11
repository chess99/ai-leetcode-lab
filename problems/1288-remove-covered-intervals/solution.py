# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:37:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        rightmost = -1
        remaining = 0
        for _, end in sorted(intervals, key=lambda interval: (interval[0], -interval[1])):
            if end > rightmost:
                remaining += 1
                rightmost = end
        return remaining
