# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:12Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []

        counts = Counter(changed)
        original = []

        for value in sorted(counts):
            if value == 0:
                if counts[value] % 2:
                    return []
                original.extend([0] * (counts[value] // 2))
                continue

            amount = counts[value]
            if amount > counts[2 * value]:
                return []
            counts[2 * value] -= amount
            original.extend([value] * amount)

        return original
