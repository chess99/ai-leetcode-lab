# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:34Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        novalethri = (occupiedIntervals, freeStart, freeEnd)
        merged = []
        for start, end in sorted(occupiedIntervals):
            if merged and start <= merged[-1][1] + 1:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        answer = []
        for start, end in merged:
            if start < freeStart:
                left_end = min(end, freeStart - 1)
                if start <= left_end:
                    answer.append([start, left_end])
            if end > freeEnd:
                right_start = max(start, freeEnd + 1)
                if right_start <= end:
                    answer.append([right_start, end])
        return answer
