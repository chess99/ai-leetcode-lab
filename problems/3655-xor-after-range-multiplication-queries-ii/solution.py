# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod=1_000_000_007;n=len(nums);B=int(n**.5)+1
        small={}
        for l,r,k,v in queries:
            if k<=B:small.setdefault(k,[]).append((l,r,v))
            else:
                for i in range(l,r+1,k):nums[i]=nums[i]*v%mod
        # For fixed step k, a query is a multiplicative range update on one
        # residue class. Difference factors are accumulated then propagated.
        for k,qs in small.items():
            diff=[1]*(n+k)
            for l,r,v in qs:
                diff[l]=diff[l]*v%mod
                end=l+((r-l)//k+1)*k
                if end<n:diff[end]=diff[end]*pow(v,mod-2,mod)%mod
            for i in range(n):
                if i>=k:diff[i]=diff[i]*diff[i-k]%mod
                nums[i]=nums[i]*diff[i]%mod
        ans=0
        for x in nums:ans^=x
        return ans
