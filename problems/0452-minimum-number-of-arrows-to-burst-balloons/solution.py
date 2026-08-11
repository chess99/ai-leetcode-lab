# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:05:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:return 0
        points.sort(key=lambda point:point[1]);arrows=1;end=points[0][1]
        for start,finish in points[1:]:
            if start>end:arrows+=1;end=finish
        return arrows
