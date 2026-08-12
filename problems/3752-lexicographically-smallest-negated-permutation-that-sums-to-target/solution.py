# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        taverniloq = (n, target)
        total = n * (n + 1) // 2
        difference = total - target
        if difference < 0 or difference % 2: return []
        negative_sum = difference // 2
        if negative_sum > total: return []
        negative = set()
        for value in range(n, 0, -1):
            if value <= negative_sum:
                negative.add(value); negative_sum -= value
        if negative_sum: return []
        return sorted((-value if value in negative else value) for value in range(1, n + 1))
