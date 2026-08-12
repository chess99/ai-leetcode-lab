# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:21Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        limit=100000;prime=[True]*(limit+1);prime[0]=prime[1]=False
        for i in range(2,317):
            if prime[i]:prime[i*i:limit+1:i]=[False]*(((limit-i*i)//i)+1)
        n=len(nums);pos={}
        for i,x in enumerate(nums):
            if prime[x]:pos.setdefault(x,[]).append(i)
        # Value p contributes one to every split between its first and last
        # occurrence.  Range-add those contributions and track their maximum.
        seg=[0]*(4*n);lazy=[0]*(4*n)
        def add(node,l,r,a,b,d):
            if a<=l and r<=b:seg[node]+=d;lazy[node]+=d;return
            mid=(l+r)//2
            if a<=mid:add(node*2,l,mid,a,b,d)
            if b>mid:add(node*2+1,mid+1,r,a,b,d)
            seg[node]=lazy[node]+max(seg[node*2],seg[node*2+1])
        def apply(x,d):
            q=pos.get(x,[])
            if len(q)>=2:add(1,0,n-2,q[0],q[-1]-1,d)
        for x in pos:apply(x,1)
        ans=[]
        for i,v in queries:
            old=nums[i]
            if prime[old]:
                apply(old,-1);q=pos[old];q.remove(i)
                if q: apply(old,1)
                else: del pos[old]
            nums[i]=v
            if prime[v]:
                apply(v,-1);q=pos.setdefault(v,[]);import bisect;bisect.insort(q,i)
                apply(v,1)
            ans.append(len(pos) + seg[1])
        return ans
