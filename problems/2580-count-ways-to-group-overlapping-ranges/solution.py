# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:27Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        groups = 0
        current_end = -1
        for start, end in ranges:
            if start > current_end:
                groups += 1
            current_end = max(current_end, end)
        return pow(2, groups, 1_000_000_007)
