# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def findMaximumScore(self, nums: List[int]) -> int:
  best=ans=0
  for x in nums[:-1]:best=max(best,x);ans+=best
  return ans
