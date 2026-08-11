# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def maximumCandies(self,candies:List[int],k:int)->int:
  lo,hi=1,max(candies)
  while lo<=hi:
   mid=(lo+hi)//2
   if sum(x//mid for x in candies)>=k: lo=mid+1
   else: hi=mid-1
  return hi
