# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:31:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        previous, current = 0, 0
        for amount in nums:
            previous, current = current, max(current, previous + amount)
        return current
