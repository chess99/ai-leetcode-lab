# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def span(bars):
            bars.sort()
            best = run = 1
            for i in range(1, len(bars)):
                run = run + 1 if bars[i] == bars[i - 1] + 1 else 1
                best = max(best, run)
            return best + 1
        side = min(span(hBars), span(vBars))
        return side * side
