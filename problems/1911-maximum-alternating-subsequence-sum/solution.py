# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:04Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        plus_state = 0
        minus_state = 0

        for value in nums:
            next_plus = max(plus_state, minus_state + value)
            next_minus = max(minus_state, plus_state - value)
            plus_state, minus_state = next_plus, next_minus

        return plus_state
