# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:22Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left, bisect_right
from typing import List


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.positions = {}
        for index, value in enumerate(arr):
            self.positions.setdefault(value, []).append(index)

    def query(self, left: int, right: int, value: int) -> int:
        indices = self.positions.get(value, [])
        return bisect_right(indices, right) - bisect_left(indices, left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
