# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:25Z
# Experiment: ai-leetcode-lab, round 1

from bisect import bisect_left
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        count = len(potions)
        answer = []

        for spell in spells:
            needed = (success + spell - 1) // spell
            answer.append(count - bisect_left(potions, needed))

        return answer
