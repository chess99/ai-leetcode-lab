# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def maxScore(self, grid: List[List[int]]) -> int:
  cols=[10**18]*len(grid[0]); ans=-10**18
  for row in grid:
   prefix=10**18
   for j,x in enumerate(row):
    previous=min(prefix,cols[j]); ans=max(ans,x-previous)
    prefix=min(previous,x);cols[j]=prefix
  return ans
