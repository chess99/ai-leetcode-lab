# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # Binary-search the maximum allowed difference.  For a candidate D,
        # values adjacent to a missing run constrain the two global choices.
        fixed=0
        for i in range(1,len(nums)):
            if nums[i]>=0 and nums[i-1]>=0:fixed=max(fixed,abs(nums[i]-nums[i-1]))
        def ok(d):
            boundaries=[]
            for i,x in enumerate(nums):
                if x==-1:
                    if i and nums[i-1]!=-1:boundaries.append(nums[i-1])
                    if i+1<len(nums) and nums[i+1]!=-1:boundaries.append(nums[i+1])
            if not boundaries:return True
            choices=(min(boundaries)+d,max(boundaries)-d)
            i=0
            while i<len(nums):
                if nums[i]!=-1:i+=1;continue
                left=nums[i-1] if i else None;start=i
                while i<len(nums) and nums[i]==-1:i+=1
                right=nums[i] if i<len(nums) else None;length=i-start
                if length==1:
                    if not any((left is None or abs(left-v)<=d) and (right is None or abs(right-v)<=d) for v in choices):return False
                else:
                    first=[v for v in choices if left is None or abs(left-v)<=d]
                    second=[v for v in choices if right is None or abs(right-v)<=d]
                    if not any(abs(x-y)<=d for x in first for y in second):return False
            return True
        lo,hi=fixed,10**9
        while lo<hi:
            mid=(lo+hi)//2
            if ok(mid):hi=mid
            else:lo=mid+1
        return lo
