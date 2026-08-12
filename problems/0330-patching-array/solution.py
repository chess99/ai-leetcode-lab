# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missing = 1
        index = patches = 0
        while missing <= n:
            if index < len(nums) and nums[index] <= missing:
                missing += nums[index]
                index += 1
            else:
                missing += missing
                patches += 1
        return patches
