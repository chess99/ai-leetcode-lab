# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:34Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        current = 0
        for value in sorted(arr):
            current = min(current + 1, value)
        return current
