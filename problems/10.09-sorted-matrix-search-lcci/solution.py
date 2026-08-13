# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:58Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:return False
        r,c=0,len(matrix[0])-1
        while r<len(matrix) and c>=0:
            if matrix[r][c]==target:return True
            if matrix[r][c]>target:c-=1
            else:r+=1
        return False
