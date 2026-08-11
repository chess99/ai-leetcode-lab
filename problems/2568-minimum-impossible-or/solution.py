# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        available = set(nums)
        value = 1
        while value in available:
            value <<= 1
        return value
