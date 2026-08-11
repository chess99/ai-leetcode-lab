# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
  rows=list(map(sum,grid)); cols=[sum(row[j] for row in grid) for j in range(len(grid[0]))]
  return sum((rows[i]-1)*(cols[j]-1) for i,row in enumerate(grid) for j,x in enumerate(row) if x)
