# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def maxPossibleScore(self, start: List[int], d: int) -> int:
  start.sort()
  def ok(x):
   last=-10**30
   for a in start:
    last=max(a,last+x)
    if last>a+d:return False
   return True
  lo,hi=0,(start[-1]+d-start[0])//(len(start)-1) if len(start)>1 else 0
  while lo<hi:
   mid=(lo+hi+1)//2
   if ok(mid):lo=mid
   else:hi=mid-1
  return lo
