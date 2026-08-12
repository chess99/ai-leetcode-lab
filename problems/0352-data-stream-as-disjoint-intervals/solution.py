# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:13Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List


class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        index = bisect_left(self.intervals, [value])
        if index and self.intervals[index - 1][1] >= value:
            return
        start = end = value
        if index and self.intervals[index - 1][1] + 1 == value:
            index -= 1
            start = self.intervals[index][0]
            self.intervals.pop(index)
        if index < len(self.intervals) and self.intervals[index][0] <= value + 1:
            end = self.intervals[index][1]
            self.intervals.pop(index)
        self.intervals.insert(index, [start, end])

    def getIntervals(self) -> List[List[int]]:
        return [interval[:] for interval in self.intervals]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
