# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:19Z
# Experiment: ai-leetcode-lab, round 1

from heapq import heappop, heappush
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        ended: list[tuple[int, int]] = []
        best_completed = 0
        answer = 0
        for start, end, value in events:
            while ended and ended[0][0] < start:
                best_completed = max(best_completed, heappop(ended)[1])
            answer = max(answer, best_completed + value)
            heappush(ended, (end, value))
        return answer
