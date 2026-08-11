# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:10:25Z
# Experiment: ai-leetcode-lab, round 1
from math import cos, pi, sin, sqrt
from random import random
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        angle = 2 * pi * random()
        distance = self.radius * sqrt(random())
        return [
            self.x_center + distance * cos(angle),
            self.y_center + distance * sin(angle),
        ]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
