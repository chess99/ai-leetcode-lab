# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:00:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort(); moves=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]: moves+=nums[i-1]+1-nums[i];nums[i]=nums[i-1]+1
        return moves
