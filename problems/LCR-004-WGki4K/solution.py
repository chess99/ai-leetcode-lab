# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = twos = 0
        mask = (1 << 32) - 1
        for value in nums:
            value &= mask
            ones = (ones ^ value) & ~twos & mask
            twos = (twos ^ value) & ~ones & mask
        return ones if ones < (1 << 31) else ones - (1 << 32)
