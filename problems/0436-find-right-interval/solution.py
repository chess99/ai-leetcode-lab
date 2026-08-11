# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:03:07Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts_with_indices = sorted(
            (start, index) for index, (start, _) in enumerate(intervals)
        )
        starts = [start for start, _ in starts_with_indices]
        result = []
        for _, end in intervals:
            position = bisect_left(starts, end)
            result.append(
                -1 if position == len(starts) else starts_with_indices[position][1]
            )
        return result
