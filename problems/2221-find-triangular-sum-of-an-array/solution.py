# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def triangularSum(self, nums: List[int]) -> int:
  while len(nums)>1: nums=[(nums[i]+nums[i+1])%10 for i in range(len(nums)-1)]
  return nums[0]
