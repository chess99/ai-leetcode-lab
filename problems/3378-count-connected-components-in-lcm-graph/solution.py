# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        n=len(nums);parent=list(range(n));owner={}
        def find(x):
            while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
            return x
        def union(a,b):
            a,b=find(a),find(b)
            if a!=b:parent[a]=b
        for i,x in enumerate(nums):
            if x<=threshold:
                if x in owner:union(i,owner[x])
                owner[x]=i
        buckets=[[]for _ in range(threshold+1)]
        for value,i in owner.items():
            for multiple in range(value,threshold+1,value):buckets[multiple].append(i)
        for a in buckets:
            for x in a[1:]:union(a[0],x)
        return len({find(i)for i in range(n)})
