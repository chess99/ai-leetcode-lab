# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:05:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        best = last = 0
        for i, fort in enumerate(forts):
            if fort:
                if forts[last] == -fort: best = max(best, i-last-1)
                last = i
        return best
