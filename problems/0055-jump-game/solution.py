# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:12:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        for index, jump in enumerate(nums):
            if index > furthest:
                return False
            furthest = max(furthest, index + jump)
            if furthest >= len(nums) - 1:
                return True
        return True
