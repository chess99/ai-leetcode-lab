# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums_odd = sorted(value for value in nums if value & 1)
        nums_even = sorted(value for value in nums if not value & 1)
        target_odd = sorted(value for value in target if value & 1)
        target_even = sorted(value for value in target if not value & 1)
        positive_change = 0
        for current, wanted in zip(nums_odd + nums_even,
                                   target_odd + target_even):
            if current > wanted:
                positive_change += (current - wanted) // 2
        return positive_change
