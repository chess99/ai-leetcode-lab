# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:37:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def countSquares(self,matrix:List[List[int]])->int:
  total=0
  for r in range(len(matrix)):
   for c in range(len(matrix[0])):
    if matrix[r][c] and r and c: matrix[r][c]=1+min(matrix[r-1][c],matrix[r][c-1],matrix[r-1][c-1])
    total+=matrix[r][c]
  return total
