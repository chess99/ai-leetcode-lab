# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def sumDigitDifferences(self, nums: List[int]) -> int:
  ans=0
  while nums[0]:
   cnt=[0]*10
   for i,x in enumerate(nums):cnt[x%10]+=1;nums[i]=x//10
   ans+=(len(nums)**2-sum(x*x for x in cnt))//2
  return ans
