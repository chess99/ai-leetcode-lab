# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        upper = len(nums) + 2
        xor = 0
        for number in range(1, upper + 1):
            xor ^= number
        for number in nums:
            xor ^= number
        distinguishing_bit = xor & -xor
        first = 0
        for number in range(1, upper + 1):
            if number & distinguishing_bit:
                first ^= number
        for number in nums:
            if number & distinguishing_bit:
                first ^= number
        return [first, xor ^ first]
