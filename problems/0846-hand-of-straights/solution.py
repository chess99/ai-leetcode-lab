# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:50:04Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False
        counts = Counter(hand)
        for start in sorted(counts):
            if counts[start]:
                needed = counts[start]
                for value in range(start, start + groupSize):
                    if counts[value] < needed: return False
                    counts[value] -= needed
        return True
