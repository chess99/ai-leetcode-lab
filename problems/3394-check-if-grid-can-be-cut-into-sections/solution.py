# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def has_three_groups(intervals):
            intervals.sort()
            groups, end = 0, -1
            for start, finish in intervals:
                if start >= end:
                    groups += 1
                    end = finish
                else:
                    end = max(end, finish)
            return groups >= 3
        return has_three_groups([(x1, x2) for x1, _, x2, _ in rectangles]) or has_three_groups([(y1, y2) for _, y1, _, y2 in rectangles])
