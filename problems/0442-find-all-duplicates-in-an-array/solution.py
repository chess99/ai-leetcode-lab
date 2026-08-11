# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:03:34Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def findDuplicates(self,nums:List[int])->List[int]:
  r=[]
  for x in nums:
   i=abs(x)-1
   if nums[i]<0:r.append(abs(x))
   else:nums[i]=-nums[i]
  return r
