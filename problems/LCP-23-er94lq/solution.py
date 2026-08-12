# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def isMagic(self, target: List[int]) -> bool:
        cards = list(range(1, len(target) + 1))
        shuffled = cards[1::2] + cards[::2]
        k = 0
        while k < len(target) and shuffled[k] == target[k]:
            k += 1
        if k == 0:
            return False

        cards = list(range(1, len(target) + 1))
        taken = 0
        while cards:
            cards = cards[1::2] + cards[::2]
            count = min(k, len(cards))
            if cards[:count] != target[taken:taken + count]:
                return False
            taken += count
            cards = cards[count:]
        return True
