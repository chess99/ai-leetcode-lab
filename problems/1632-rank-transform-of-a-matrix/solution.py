# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:35Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        rows,columns=len(matrix),len(matrix[0]);groups=defaultdict(list)
        for r in range(rows):
            for c in range(columns):groups[matrix[r][c]].append((r,c))
        rank=[0]*(rows+columns);answer=[[0]*columns for _ in range(rows)]
        for value in sorted(groups):
            cells=groups[value];parent={}
            def find(x):
                parent.setdefault(x,x)
                if parent[x]!=x:parent[x]=find(parent[x])
                return parent[x]
            for r,c in cells:parent[find(r)]=find(rows+c)
            component=defaultdict(list)
            for r,c in cells:component[find(r)].append((r,c))
            updates=[]
            for members in component.values():
                current=1+max(max(rank[r],rank[rows+c]) for r,c in members)
                for r,c in members:answer[r][c]=current;updates.append((r,c,current))
            for r,c,current in updates:rank[r]=rank[rows+c]=max(rank[r],current)
        return answer
