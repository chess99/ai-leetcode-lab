# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:39:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1: break
            total += nums[i]
        seen = set(nums)
        while total in seen: total += 1
        return total
