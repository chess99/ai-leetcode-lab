# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)

        while left < right:
            maximum = (left + right) // 2
            stores_needed = sum(
                (quantity + maximum - 1) // maximum for quantity in quantities
            )
            if stores_needed <= n:
                right = maximum
            else:
                left = maximum + 1

        return left
