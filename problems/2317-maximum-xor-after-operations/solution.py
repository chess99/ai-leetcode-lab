# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        maximum = 0

        for number in nums:
            maximum |= number

        return maximum
