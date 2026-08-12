# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted(value * value for value in nums)
        negative = len(nums) // 2
        return sum(squares[negative:]) - sum(squares[:negative])
