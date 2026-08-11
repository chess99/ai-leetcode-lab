# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:12:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted((a, b, c))
        left_gap = b - a
        right_gap = c - b
        if left_gap == 1 and right_gap == 1:
            return [0, 0]
        minimum = 1 if left_gap <= 2 or right_gap <= 2 else 2
        maximum = max(left_gap, right_gap) - 1
        return [minimum, maximum]
