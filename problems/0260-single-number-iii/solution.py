# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:44:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for value in nums: xor ^= value
        bit = xor & -xor
        first = second = 0
        for value in nums:
            if value & bit: first ^= value
            else: second ^= value
        return [first, second]
