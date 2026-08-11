# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def minimumCost(self, nums: List[int]) -> int:
  x=sorted(nums)[len(nums)//2]; candidates=[]
  for delta in range(-2,3):
   p=int(str(max(0,x+delta))[:(len(str(max(0,x+delta)))+1)//2] or 0)
   for q in (p-1,p,p+1):
    if q>=0:
     t=str(q); candidates.append(int(t+t[-2::-1] if len(t)>1 else t))
     candidates.append(int(t+t[::-1]))
  return min(sum(abs(a-y) for a in nums) for y in candidates if y<10**9)
