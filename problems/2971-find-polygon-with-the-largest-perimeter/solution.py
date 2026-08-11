# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def largestPerimeter(self, nums: List[int]) -> int:
  nums.sort(); total=sum(nums)
  for i in range(len(nums)-1,1,-1):
   if total-nums[i]>nums[i]: return total
   total-=nums[i]
  return -1
