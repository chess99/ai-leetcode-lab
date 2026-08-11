# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        previous = bottom - 1
        longest = 0

        for floor in sorted(special):
            longest = max(longest, floor - previous - 1)
            previous = floor

        return max(longest, top - previous)
