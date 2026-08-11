# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:11:17Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from random import randint
from typing import List


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix_counts = []
        total = 0
        for left, bottom, right, top in rects:
            total += (right - left + 1) * (top - bottom + 1)
            self.prefix_counts.append(total)

    def pick(self) -> List[int]:
        point_index = randint(1, self.prefix_counts[-1])
        rectangle_index = bisect_left(self.prefix_counts, point_index)
        left, bottom, right, top = self.rects[rectangle_index]
        width = right - left + 1
        offset = point_index - (
            self.prefix_counts[rectangle_index - 1] if rectangle_index else 0
        ) - 1
        return [left + offset % width, bottom + offset // width]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
