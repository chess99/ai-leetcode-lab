# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:52:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        def maximum_gap(cuts: List[int], length: int) -> int:
            cuts = [0] + sorted(cuts) + [length]
            return max(b - a for a, b in zip(cuts, cuts[1:]))
        return maximum_gap(horizontalCuts, h) * maximum_gap(verticalCuts, w) % (10 ** 9 + 7)
