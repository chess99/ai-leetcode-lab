# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n=len(nums);p=list(range(n))
        def find(x):
            while p[x]!=x:p[x]=p[p[x]];x=p[x]
            return x
        for a,b in swaps:
            a,b=find(a),find(b)
            if a!=b:p[a]=b
        groups={}
        for i,x in enumerate(nums):groups.setdefault(find(i),[]).append(i)
        ans=0
        for ind in groups.values():
            vals=sorted((nums[i]for i in ind),reverse=True);plus=sum(i%2==0 for i in ind)
            ans+=sum(vals[:plus])-sum(vals[plus:])
        return ans
