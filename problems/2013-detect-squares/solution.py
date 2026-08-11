# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:13Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class DetectSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        squares = 0
        for (diagonal_x, diagonal_y), diagonal_count in self.points.items():
            if (diagonal_x == x
                    or abs(diagonal_x - x) != abs(diagonal_y - y)):
                continue
            squares += (diagonal_count
                        * self.points[(x, diagonal_y)]
                        * self.points[(diagonal_x, y)])
        return squares


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
