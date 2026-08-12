# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        from bisect import bisect_left, bisect_right
        from collections import Counter
        nums.sort();cnt=Counter(nums);ans=0;l=0
        # The target may be absent: then every contributing element consumes
        # an operation, and its reachable intervals only need a common point.
        for r,x in enumerate(nums):
            while nums[l]<x-2*k:l+=1
            ans=max(ans,min(r-l+1,numOperations))
        # For an existing target x, its current copies consume no operations.
        for x, current in cnt.items():
            reachable=bisect_right(nums,x+k)-bisect_left(nums,x-k)
            ans=max(ans,min(reachable,current+numOperations))
        return ans
