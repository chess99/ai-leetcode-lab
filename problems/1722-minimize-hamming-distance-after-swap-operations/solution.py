# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:24Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter, defaultdict
from typing import List
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent=list(range(len(source)))
        def find(x):
            while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
            return x
        for a,b in allowedSwaps:parent[find(a)]=find(b)
        groups=defaultdict(Counter)
        for i,value in enumerate(source):groups[find(i)][value]+=1
        answer=0
        for i,value in enumerate(target):
            group=groups[find(i)]
            if group[value]:group[value]-=1
            else:answer+=1
        return answer
