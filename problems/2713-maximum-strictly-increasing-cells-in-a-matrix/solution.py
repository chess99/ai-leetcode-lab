# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        from collections import defaultdict
        d=defaultdict(list);m,n=len(mat),len(mat[0]);row=[0]*m;col=[0]*n;ans=0
        for i in range(m):
            for j in range(n):d[mat[i][j]].append((i,j))
        for value in sorted(d):
            cells=d[value]
            vals=[max(row[i],col[j])+1 for i,j in cells]
            for (i,j),v in zip(cells,vals):row[i]=max(row[i],v);col[j]=max(col[j],v);ans=max(ans,v)
        return ans
