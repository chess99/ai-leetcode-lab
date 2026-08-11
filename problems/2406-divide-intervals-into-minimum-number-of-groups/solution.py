# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:13Z
# Experiment: ai-leetcode-lab, round 1

from heapq import heappop, heappush
from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        ends = []
        for start, end in sorted(intervals):
            if ends and ends[0] < start:
                heappop(ends)
            heappush(ends, end)
        return len(ends)
