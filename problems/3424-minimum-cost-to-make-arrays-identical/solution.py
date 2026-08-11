# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        direct = sum(abs(a - b) for a, b in zip(arr, brr))
        rearranged = k + sum(abs(a - b) for a, b in zip(sorted(arr), sorted(brr)))
        return min(direct, rearranged)
