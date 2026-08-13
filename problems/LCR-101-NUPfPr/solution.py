# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:39:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        possible = {0}
        for num in nums:
            possible |= {value + num for value in possible if value + num <= target}
        return target in possible
