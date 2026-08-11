# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:05:39Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        groups=defaultdict(list); answer=float('inf')
        for i,(x1,y1) in enumerate(points):
            for x2,y2 in points[:i]: groups[(x1+x2,y1+y2,(x1-x2)**2+(y1-y2)**2)].append(((x1,y1),(x2,y2)))
        for pairs in groups.values():
            for i,((x1,y1),(x2,y2)) in enumerate(pairs):
                for (x3,y3),_ in pairs[:i]: answer=min(answer,((x1-x3)**2+(y1-y3)**2)**.5*((x2-x3)**2+(y2-y3)**2)**.5)
        return 0 if answer==float('inf') else answer
