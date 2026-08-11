# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        best = {}
        for a, b in zip(x, y): best[a] = max(best.get(a, -1), b)
        values = sorted(best.values(), reverse=True)
        return sum(values[:3]) if len(values) >= 3 else -1
