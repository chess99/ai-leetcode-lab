# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:00:11Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        columns=defaultdict(list)
        for x,y in points: columns[x].append(y)
        last={}; best=float('inf')
        for x in sorted(columns):
            ys=sorted(columns[x])
            for i in range(len(ys)):
                for j in range(i):
                    pair=(ys[j],ys[i])
                    if pair in last: best=min(best,(x-last[pair])*(ys[i]-ys[j]))
                    last[pair]=x
        return 0 if best==float('inf') else best
