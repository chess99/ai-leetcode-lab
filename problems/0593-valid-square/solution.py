# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:24:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = (p1, p2, p3, p4)
        distances = sorted(
            (first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2
            for index, first in enumerate(points)
            for second in points[index + 1:]
        )
        return distances[0] > 0 and distances[:4] == [distances[0]] * 4 and distances[4:] == [distances[4]] * 2
