# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from functools import cmp_to_key

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        parts = [bin(value)[2:] for value in nums]
        parts.sort(key=cmp_to_key(lambda a, b: -1 if a + b > b + a else (1 if a + b < b + a else 0)))
        return int("".join(parts), 2)
