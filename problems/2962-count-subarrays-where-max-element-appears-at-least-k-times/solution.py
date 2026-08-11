# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def countSubarrays(self, nums: List[int], k: int) -> int:
  mx=max(nums); left=count=ans=0
  for x in nums:
   count += x==mx
   while count>=k:
    count -= nums[left]==mx; left+=1
   ans += left
  return ans
