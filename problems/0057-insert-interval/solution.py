# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:12:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        index = 0
        while index < len(intervals) and intervals[index][1] < newInterval[0]:
            merged.append(intervals[index])
            index += 1
        while index < len(intervals) and intervals[index][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index += 1
        merged.append(newInterval)
        merged.extend(intervals[index:])
        return merged
