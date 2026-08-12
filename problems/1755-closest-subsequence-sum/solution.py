# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:42Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        from bisect import bisect_left
        mid=len(nums)//2;a=[0];b=[0]
        for x in nums[:mid]:a += [v+x for v in a]
        for x in nums[mid:]:b += [v+x for v in b]
        b.sort();ans=10**18
        for x in a:
            i=bisect_left(b,goal-x)
            for j in (i-1,i):
                if 0<=j<len(b):ans=min(ans,abs(x+b[j]-goal))
        return ans
