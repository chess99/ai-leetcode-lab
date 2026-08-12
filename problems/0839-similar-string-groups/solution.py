# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n=len(strs);parent=list(range(n));groups=n
        def find(x):
            while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
            return x
        for i in range(n):
            for j in range(i):
                if sum(a!=b for a,b in zip(strs[i],strs[j]))<=2:
                    a,b=find(i),find(j)
                    if a!=b:parent[a]=b;groups-=1
        return groups
