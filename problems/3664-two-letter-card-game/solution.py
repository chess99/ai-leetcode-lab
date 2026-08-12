# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:45Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List

class Solution:
    def score(self, cards: List[str], x: str) -> int:
        brivolante = cards
        left = Counter()
        right = Counter()
        wildcards = 0
        for card in brivolante:
            if card == x + x:
                wildcards += 1
            elif card[0] == x:
                left[card[1]] += 1
            elif card[1] == x:
                right[card[0]] += 1

        def pairs(counts, allocated):
            ordinary = sum(counts.values())
            total = ordinary + allocated
            largest = max([allocated, *counts.values()], default=allocated)
            return min(total // 2, total - largest)

        answer = 0
        for allocated_left in range(wildcards + 1):
            answer = max(
                answer,
                pairs(left, allocated_left) + pairs(right, wildcards - allocated_left),
            )
        return answer
