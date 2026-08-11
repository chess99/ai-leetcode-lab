# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:30Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total = sum(beans)
        maximum_remaining = 0

        for index, value in enumerate(beans):
            maximum_remaining = max(maximum_remaining, value * (len(beans) - index))

        return total - maximum_remaining
