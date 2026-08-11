# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:47:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        top,bottom=0,len(mat)-1
        while top<=bottom:
            row=(top+bottom)//2;col=max(range(len(mat[0])),key=lambda c:mat[row][c])
            if row>0 and mat[row-1][col]>mat[row][col]:bottom=row-1
            elif row+1<len(mat) and mat[row+1][col]>mat[row][col]:top=row+1
            else:return [row,col]
