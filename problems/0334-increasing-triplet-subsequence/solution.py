# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:47:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        for value in nums:
            if value <= first:
                first = value
            elif value <= second:
                second = value
            else:
                return True
        return False
