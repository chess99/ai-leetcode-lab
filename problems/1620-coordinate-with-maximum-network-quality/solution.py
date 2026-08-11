# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:24Z
# Experiment: ai-leetcode-lab, round 1
from math import hypot
from typing import List
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        best, answer = -1, [0, 0]
        for x in range(51):
            for y in range(51):
                quality = sum(int(q / (1 + hypot(x-a, y-b))) for a,b,q in towers if hypot(x-a,y-b) <= radius)
                if quality > best: best, answer = quality, [x, y]
        return answer
