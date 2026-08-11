# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
  nums.sort(); mid=len(nums)//2; ans=0
  for x in nums[:mid+1]:
   if x>k: ans+=x-k
  for x in nums[mid:]:
   if x<k: ans+=k-x
  return ans
