# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:00:12Z
# Experiment: ai-leetcode-lab, round 1
from itertools import permutations
from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        best = -1
        for a, b, c, d in permutations(arr):
            value = 600 * a + 60 * b + 10 * c + d
            if value < 1440: best = max(best, value)
        return "" if best < 0 else f"{best // 60:02d}:{best % 60:02d}"
