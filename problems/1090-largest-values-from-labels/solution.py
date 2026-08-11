# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:21:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        used = {}
        total = 0
        chosen = 0
        for value, label in sorted(zip(values, labels), reverse=True):
            if used.get(label, 0) == useLimit:
                continue
            total += value
            used[label] = used.get(label, 0) + 1
            chosen += 1
            if chosen == numWanted:
                break
        return total
