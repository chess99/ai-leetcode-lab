# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n=len(nums);bit=[[0]*(n+1)for _ in range(6)]
        def depth(x):
            d=0
            while x!=1:x=x.bit_count();d+=1
            return d
        def add(d,i,v):
            i+=1
            while i<=n:bit[d][i]+=v;i+=i&-i
        def get(d,i):
            s=0;i+=1
            while i:s+=bit[d][i];i-=i&-i
            return s
        ds=[depth(x)for x in nums]
        for i,d in enumerate(ds):add(d,i,1)
        ans=[]
        for q in queries:
            if q[0]==1:ans.append(get(q[3],q[2])-get(q[3],q[1]-1))
            else:
                i,x=q[1],q[2];add(ds[i],i,-1);ds[i]=depth(x);add(ds[i],i,1)
        return ans
