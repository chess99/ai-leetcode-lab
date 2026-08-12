# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        vals=sorted(set(nums));rank={x:i+1 for i,x in enumerate(vals)};n=len(vals)
        a=[nums[0]];b=[nums[1]];fa=[0]*(n+1);fb=[0]*(n+1)
        def add(f,i):
            while i<=n:f[i]+=1;i+=i&-i
        def sm(f,i):
            s=0
            while i:s+=f[i];i-=i&-i
            return s
        add(fa,rank[nums[0]]);add(fb,rank[nums[1]])
        for x in nums[2:]:
            r=rank[x];ga=len(a)-sm(fa,r);gb=len(b)-sm(fb,r)
            if ga>gb or ga==gb and len(a)<=len(b):a.append(x);add(fa,r)
            else:b.append(x);add(fb,r)
        return a+b
