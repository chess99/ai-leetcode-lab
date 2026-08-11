# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n=len(properties); parent=list(range(n))
        def find(x):
            while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
            return x
        for i in range(n):
            a=set(properties[i])
            for j in range(i):
                if len(a & set(properties[j]))>=k:
                    x,y=find(i),find(j)
                    if x!=y: parent[x]=y
        return len({find(i) for i in range(n)})
