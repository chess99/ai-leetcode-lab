# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:15Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        need=len(set(nums)); count=Counter(); left=ans=0
        for right,x in enumerate(nums):
            count[x]+=1
            while len(count)==need:
                ans+=len(nums)-right; count[nums[left]]-=1
                if not count[nums[left]]: del count[nums[left]]
                left+=1
        return ans
