# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans=left=total=0
        for r,x in enumerate(nums):
            total+=x
            while total*(r-left+1)>=k:total-=nums[left];left+=1
            ans+=r-left+1
        return ans
