# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:23Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix=[[0]*len(colSum) for _ in rowSum];row=col=0
        while row<len(rowSum) and col<len(colSum):
            value=min(rowSum[row],colSum[col]);matrix[row][col]=value;rowSum[row]-=value;colSum[col]-=value
            if rowSum[row]==0:row+=1
            if colSum[col]==0:col+=1
        return matrix
