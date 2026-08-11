# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        return len(nums)<=2 or any(a+b>=m for a,b in zip(nums,nums[1:]))
