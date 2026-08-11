# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        day = 0
        last_completed = {}

        for task in tasks:
            day += 1
            if task in last_completed:
                day = max(day, last_completed[task] + space + 1)
            last_completed[task] = day

        return day
