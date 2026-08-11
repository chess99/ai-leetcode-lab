# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:26:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = twos = 0
        for value in nums:
            ones = (ones ^ value) & ~twos
            twos = (twos ^ value) & ~ones
        return ones
