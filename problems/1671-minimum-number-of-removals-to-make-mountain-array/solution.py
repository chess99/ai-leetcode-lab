# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        from bisect import bisect_left
        def lis(a):
            t=[];r=[]
            for x in a:
                i=bisect_left(t,x)
                if i==len(t):t.append(x)
                else:t[i]=x
                r.append(i+1)
            return r
        a=lis(nums);b=lis(nums[::-1])[::-1];return len(nums)-max(a[i]+b[i]-1 for i in range(len(nums))if a[i]>1 and b[i]>1)
