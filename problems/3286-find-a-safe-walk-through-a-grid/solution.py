# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import deque
class Solution:
 def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
  m,n=len(grid),len(grid[0]);q=deque([(0,0,health-grid[0][0])]);seen=[[-1]*n for _ in range(m)]
  while q:
   i,j,h=q.popleft()
   if h<=0 or h<=seen[i][j]:continue
   seen[i][j]=h
   if (i,j)==(m-1,n-1):return True
   for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
    if 0<=x<m and 0<=y<n and h-grid[x][y]>seen[x][y]:q.append((x,y,h-grid[x][y]))
  return False
