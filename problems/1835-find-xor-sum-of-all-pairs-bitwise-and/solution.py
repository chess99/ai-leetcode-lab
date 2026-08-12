# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:47Z
# Experiment: ai-leetcode-lab, round 1
from functools import reduce
from operator import xor
from typing import List


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        return reduce(xor, arr1, 0) & reduce(xor, arr2, 0)
