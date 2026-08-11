# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def minimumOperations(self, grid: List[List[int]]) -> int:
  m,n=len(grid),len(grid[0]); dp=[0]*10
  for j in range(n):
   cnt=[0]*10
   for i in range(m):cnt[grid[i][j]]+=1
   nd=[m-cnt[x]+min(dp[y] for y in range(10) if y!=x) if j else m-cnt[x] for x in range(10)]
   dp=nd
  return min(dp)
