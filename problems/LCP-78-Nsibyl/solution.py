# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def rampartDefensiveLine(self, rampart: List[List[int]]) -> int:
        gaps = [rampart[i + 1][0] - rampart[i][1] for i in range(len(rampart) - 1)]

        def possible(expansion: int) -> bool:
            previous_right = 0
            for gap in gaps[:-1]:
                left_capacity = gap - previous_right
                if left_capacity < 0:
                    return False
                used_left = min(expansion, left_capacity)
                previous_right = expansion - used_left
            return previous_right <= gaps[-1]

        low, high = 0, sum(gaps) + 1
        while low + 1 < high:
            middle = (low + high) // 2
            if possible(middle):
                low = middle
            else:
                high = middle
        return low
