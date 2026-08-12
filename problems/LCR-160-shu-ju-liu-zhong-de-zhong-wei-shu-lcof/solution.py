# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:28Z
# Experiment: ai-leetcode-lab, round 1
from heapq import heappop, heappush


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        if not self.lower or num <= -self.lower[0]:
            heappush(self.lower, -num)
        else:
            heappush(self.upper, num)
        if len(self.lower) > len(self.upper) + 1:
            heappush(self.upper, -heappop(self.lower))
        elif len(self.upper) > len(self.lower):
            heappush(self.lower, -heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return float(-self.lower[0])
        return (-self.lower[0] + self.upper[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
