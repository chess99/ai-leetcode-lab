# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def containsNearbyAlmostDuplicate(self,nums:List[int],k:int,t:int)->bool:
  if k <= 0 or t < 0:return False
  b={};w=t+1
  for i,x in enumerate(nums):
   q=x//w
   if q in b or q-1 in b and x-b[q-1]<=t or q+1 in b and b[q+1]-x<=t:return True
   b[q]=x
   if i>=k:del b[nums[i-k]//w]
  return False
