# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:04Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        m=max(nums); parent=list(range(m+1))
        def find(x):
            while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
            return x
        def union(a,b):
            a,b=find(a),find(b)
            if a!=b: parent[a]=b
        sp=list(range(m+1))
        for i in range(2,m+1):
            if sp[i]==i:
                for j in range(i*i,m+1,i):
                    if sp[j]==j: sp[j]=i
        for x in nums:
            y=x
            while y>1:
                p=sp[y]; union(x,p)
                while y%p==0:y//=p
        return all(find(a)==find(b) for a,b in zip(nums,sorted(nums)))
