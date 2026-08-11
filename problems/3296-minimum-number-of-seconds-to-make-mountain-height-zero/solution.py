# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from math import isqrt
class Solution:
 def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
  def ok(t):
   total=0
   for w in workerTimes:
    q=t//w; total+=(isqrt(1+8*q)-1)//2
   return total>=mountainHeight
  lo,hi=0,max(workerTimes)*mountainHeight*(mountainHeight+1)//2
  while lo<hi:
   mid=(lo+hi)//2
   if ok(mid):hi=mid
   else:lo=mid+1
  return lo
