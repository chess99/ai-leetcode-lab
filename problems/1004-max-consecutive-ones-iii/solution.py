# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:08:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=zeroes=0
        for right,value in enumerate(nums):
            zeroes+=value==0
            if zeroes>k: zeroes-=nums[left]==0;left+=1
        return len(nums)-left
