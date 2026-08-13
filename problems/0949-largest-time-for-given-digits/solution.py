# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Created: 2026-08-13
# Experiment: ai-leetcode-lab, round 1
from itertools import permutations
from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        best = -1

        for a, b, c, d in permutations(arr):
            hour = 10 * a + b
            minute = 10 * c + d
            if hour < 24 and minute < 60:
                best = max(best, 60 * hour + minute)

        if best < 0:
            return ""
        return f"{best // 60:02d}:{best % 60:02d}"
