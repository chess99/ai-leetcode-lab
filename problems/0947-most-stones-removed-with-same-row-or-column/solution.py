# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:00:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent={}
        def find(x):
            parent.setdefault(x,x)
            if parent[x]!=x: parent[x]=find(parent[x])
            return parent[x]
        for row,col in stones: parent[find(row)]=find(~col)
        return len(stones)-len({find(row) for row,_ in stones})
