# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def fieldOfGreatestBlessing(self, forceField: List[List[int]]) -> int:
        rectangles = [(2 * x - side, 2 * x + side, 2 * y - side, 2 * y + side)
                      for x, y, side in forceField]
        x_coordinates = sorted({value for left, right, _, _ in rectangles for value in (left, right)})
        answer = 0
        for x in x_coordinates:
            events = []
            for left, right, bottom, top in rectangles:
                if left <= x <= right:
                    events.append((bottom, 1))
                    events.append((top, -1))
            events.sort(key=lambda item: (item[0], -item[1]))
            active = 0
            for _, change in events:
                active += change
                answer = max(answer, active)
        return answer
