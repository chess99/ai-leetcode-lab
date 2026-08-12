# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        active_first = True
        difference = 0
        for i, score in enumerate(nums):
            if score % 2:
                active_first = not active_first
            if i % 6 == 5:
                active_first = not active_first
            difference += score if active_first else -score
        return difference
