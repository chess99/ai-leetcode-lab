# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
  nums.sort(); ans=[]
  for i in range(0,len(nums),3):
   if nums[i+2]-nums[i]>k:return []
   ans.append(nums[i:i+3])
  return ans
