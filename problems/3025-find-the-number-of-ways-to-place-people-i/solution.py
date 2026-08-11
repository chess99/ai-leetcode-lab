# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        answer = 0
        for ax, ay in points:
            for bx, by in points:
                if not (ax <= bx and ay >= by) or (ax == bx and ay == by):
                    continue
                if all(
                    (px, py) in ((ax, ay), (bx, by))
                    or not (ax <= px <= bx and by <= py <= ay)
                    for px, py in points
                ):
                    answer += 1
        return answer
