# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def maximumTotalSum(self, maximumHeight: List[int]) -> int:
  maximumHeight.sort(reverse=True);last=10**30;ans=0
  for x in maximumHeight:
   last=min(last-1,x)
   if last<=0:return -1
   ans+=last
  return ans
