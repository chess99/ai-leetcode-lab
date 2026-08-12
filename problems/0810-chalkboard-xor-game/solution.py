# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:52Z
# Experiment: ai-leetcode-lab, round 1
from functools import reduce
from operator import xor
from typing import List


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        return len(nums) % 2 == 0 or reduce(xor, nums, 0) == 0
