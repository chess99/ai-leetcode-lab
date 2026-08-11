# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import defaultdict
class Solution:
 def maxSubarrayLength(self, nums: List[int], k: int) -> int:
  cnt=defaultdict(int); left=ans=0
  for right,x in enumerate(nums):
   cnt[x]+=1
   while cnt[x]>k: cnt[nums[left]]-=1; left+=1
   ans=max(ans,right-left+1)
  return ans
