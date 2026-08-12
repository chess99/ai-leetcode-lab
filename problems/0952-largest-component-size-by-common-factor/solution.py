# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:04Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        parent={}
        def find(x):
            parent.setdefault(x,x)
            if parent[x]!=x:parent[x]=find(parent[x])
            return parent[x]
        for x in nums:
            v=x;f=2
            while f*f<=v:
                if v%f==0:
                    parent[find(x)]=find(f)
                    while v%f==0:v//=f
                f+=1
            if v>1:parent[find(x)]=find(v)
        count={}
        for x in nums:count[find(x)]=count.get(find(x),0)+1
        return max(count.values())
