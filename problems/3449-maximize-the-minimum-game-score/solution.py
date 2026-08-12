# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def feasible(score: int) -> bool:
            moves = 0
            carried = 0
            last = len(points) - 1
            for i, value in enumerate(points):
                required = (score + value - 1) // value - carried
                if i < last:
                    required = max(required, 1)
                else:
                    required = max(required, 0)
                if required:
                    moves += 2 * required - 1
                carried = max(0, required - 1)
                if moves > m:
                    return False
            return True

        low, high = 0, max(points) * m
        while low < high:
            middle = (low + high + 1) // 2
            if feasible(middle):
                low = middle
            else:
                high = middle - 1
        return low
