# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort(); left=ans=0
        for right,x in enumerate(nums):
            while x-nums[left]>2*k: left+=1
            ans=max(ans,right-left+1)
        return ans
