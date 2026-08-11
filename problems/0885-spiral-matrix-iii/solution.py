# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:56:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result=[]; r,c=rStart,cStart; steps=1
        if 0<=r<rows and 0<=c<cols: result.append([r,c])
        while len(result)<rows*cols:
            for dr,dc in ((0,1),(1,0), (0,-1),(-1,0)):
                for _ in range(steps):
                    r+=dr;c+=dc
                    if 0<=r<rows and 0<=c<cols: result.append([r,c])
                if dc!=0: steps+=1
        return result
