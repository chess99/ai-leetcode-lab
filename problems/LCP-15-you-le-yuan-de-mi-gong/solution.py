# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:44Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def visitOrder(self, points: List[List[int]], direction: str) -> List[int]:
        remaining = set(range(len(points)))
        current = min(remaining, key=lambda i: (points[i][0], points[i][1]))
        answer = [current]
        remaining.remove(current)

        def cross(a, b, c):
            return ((points[b][0] - points[a][0]) *
                    (points[c][1] - points[a][1]) -
                    (points[b][1] - points[a][1]) *
                    (points[c][0] - points[a][0]))

        for wanted in direction:
            candidate = next(iter(remaining))
            for other in remaining:
                value = cross(current, candidate, other)
                if (wanted == 'L' and value < 0) or (wanted == 'R' and value > 0):
                    candidate = other
            answer.append(candidate)
            remaining.remove(candidate)
            current = candidate
        answer.append(remaining.pop())
        return answer
