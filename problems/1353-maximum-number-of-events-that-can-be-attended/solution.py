# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:42:12Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        attended = 0
        day = 0
        index = 0
        available = []
        while index < len(events) or available:
            if not available:
                day = events[index][0]
            while index < len(events) and events[index][0] <= day:
                heapq.heappush(available, events[index][1])
                index += 1
            while available and available[0] < day:
                heapq.heappop(available)
            if available:
                heapq.heappop(available)
                attended += 1
                day += 1
        return attended
