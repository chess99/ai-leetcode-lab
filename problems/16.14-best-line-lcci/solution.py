# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:01:01Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        from math import gcd
        best_count, answer = 2, [0, 1]
        for i in range(len(points)):
            lines = {}
            for j in range(i+1,len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                divisor = gcd(dx, dy)
                dx //= divisor
                dy //= divisor
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                lines.setdefault((dx, dy), []).append(j)
            for indices in lines.values():
                candidate = [i, indices[0]]
                count = len(indices) + 1
                if count > best_count or (count == best_count and candidate < answer):
                    best_count, answer = count, candidate
        return answer
