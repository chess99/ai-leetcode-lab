# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        for mask in range(1, (1 << n) - 1):
            product = 1
            for i, value in enumerate(nums):
                if mask >> i & 1:
                    product *= value
                    if product > target: break
            if product != target: continue
            other = 1
            for i, value in enumerate(nums):
                if not (mask >> i & 1):
                    other *= value
                    if other > target: break
            if other == target: return True
        return False
