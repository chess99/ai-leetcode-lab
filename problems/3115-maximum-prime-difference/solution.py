# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def maximumPrimeDifference(self, nums: List[int]) -> int:
  def prime(x): return x>1 and all(x%d for d in range(2,int(x**.5)+1))
  p=[i for i,x in enumerate(nums) if prime(x)]
  return p[-1]-p[0]
