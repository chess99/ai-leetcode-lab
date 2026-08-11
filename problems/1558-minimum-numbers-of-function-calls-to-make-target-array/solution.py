# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:14:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        increments = sum(value.bit_count() for value in nums)
        doublings = max(value.bit_length() for value in nums) - 1
        return increments + max(doublings, 0)
