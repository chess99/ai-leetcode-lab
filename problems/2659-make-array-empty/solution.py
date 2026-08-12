# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n=len(nums);order=sorted(range(n),key=lambda i:nums[i])
        # Count remaining alive positions with Fenwick for duplicate-safe rotations.
        bit=[0]*(n+1)
        def add(i,v):
            while i<=n:bit[i]+=v;i+=i&-i
        def sm(i):
            s=0
            while i:s+=bit[i];i-=i&-i
            return s
        for i in range(1,n+1):add(i,1)
        ans=0;cur=0
        for i in order:
            ans+=sm(i+1)-sm(cur) if i>=cur else sm(n)-sm(cur)+sm(i+1)
            add(i+1,-1);cur=i+1
        return ans
