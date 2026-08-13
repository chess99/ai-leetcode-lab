# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:45:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
        def lower_bound(value: int) -> int:
            left, right = 0, len(scores)
            while left < right:
                middle = (left + right) // 2
                if scores[middle] < value:
                    left = middle + 1
                else:
                    right = middle
            return left

        return lower_bound(target + 1) - lower_bound(target)
