# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
  xs=sorted(x for x,_ in points); ans=0; i=0
  while i<len(xs):
   end=xs[i]+w; ans+=1
   while i<len(xs) and xs[i]<=end:i+=1
  return ans
