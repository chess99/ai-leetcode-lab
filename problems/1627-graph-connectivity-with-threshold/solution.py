# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:34Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        parent=list(range(n+1))
        def find(x):
            while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
            return x
        for factor in range(threshold+1,n+1):
            for multiple in range(2*factor,n+1,factor):parent[find(multiple)]=find(factor)
        return [find(a)==find(b) for a,b in queries]
