# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m,n=len(mat),len(mat[0]); pos={v:(i,j) for i,row in enumerate(mat) for j,v in enumerate(row)}; rows=[0]*m; cols=[0]*n
        for i,v in enumerate(arr):
            r,c=pos[v]; rows[r]+=1; cols[c]+=1
            if rows[r]==n or cols[c]==m: return i
