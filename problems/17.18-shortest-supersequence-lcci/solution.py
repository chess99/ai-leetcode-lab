# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:22:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        needed = set(small)
        counts = {}
        covered = left = 0
        best = None
        for right, value in enumerate(big):
            if value in needed:
                counts[value] = counts.get(value, 0) + 1
                covered += counts[value] == 1
            while covered == len(needed):
                if best is None or right - left < best[1] - best[0]:
                    best = [left, right]
                outgoing = big[left]
                if outgoing in needed:
                    counts[outgoing] -= 1
                    covered -= counts[outgoing] == 0
                left += 1
        return best or []
