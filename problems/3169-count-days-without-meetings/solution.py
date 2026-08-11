# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        free = 0
        previous_end = 0
        for start, end in sorted(meetings):
            if end <= previous_end:
                continue
            free += max(0, start - previous_end - 1)
            previous_end = end
        return free + days - previous_end
