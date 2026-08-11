# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        heights=[0]*len(matrix[0]);answer=0
        for row in matrix:
            for i,value in enumerate(row):heights[i]=heights[i]+1 if value else 0
            for width,height in enumerate(sorted(heights,reverse=True),1):answer=max(answer,width*height)
        return answer
