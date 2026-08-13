# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:22:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        best=-1
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]!=1:continue
            j=i+2
            while j<len(nums) and nums[j]-nums[j-1]==(-1 if (j-i)%2==0 else 1):j+=1
            best=max(best,j-i)
        return best
