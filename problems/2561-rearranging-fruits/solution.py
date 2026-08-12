# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:33Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        difference = Counter(basket1)
        difference.subtract(basket2)
        extra = []
        for value, count in difference.items():
            if count % 2:
                return -1
            extra.extend([value] * (abs(count) // 2))
        extra.sort()
        minimum = min(min(basket1), min(basket2))
        return sum(min(value, 2 * minimum) for value in extra[:len(extra) // 2])
