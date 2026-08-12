# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        previous_two = 0
        previous_one = 0
        for money in nums:
            previous_two, previous_one = (
                previous_one,
                max(previous_one, previous_two + money),
            )
        return previous_one
