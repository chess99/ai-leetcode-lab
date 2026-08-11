# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:00:12Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        positions = deque(range(len(deck))); result = [0] * len(deck)
        for card in sorted(deck):
            result[positions.popleft()] = card
            if positions: positions.append(positions.popleft())
        return result
