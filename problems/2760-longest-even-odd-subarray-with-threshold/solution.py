# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:22:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        best=0
        for i,value in enumerate(nums):
            if value%2 or value>threshold:continue
            j=i
            while j<len(nums) and nums[j]<=threshold and (j==i or nums[j]%2!=nums[j-1]%2):j+=1
            best=max(best,j-i)
        return best
