# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort();queries=sorted((m,x,i)for i,(x,m)in enumerate(queries));root={};ans=[-1]*len(queries);j=0
        def add(x):
            node=root
            for b in range(30,-1,-1):node=node.setdefault((x>>b)&1,{})
        for m,x,i in queries:
            while j<len(nums)and nums[j]<=m:add(nums[j]);j+=1
            if not root:continue
            node=root;v=0
            for b in range(30,-1,-1):
                bit=(x>>b)&1;want=1-bit
                if want in node:v|=1<<b;node=node[want]
                else:node=node[bit]
            ans[i]=v
        return ans
