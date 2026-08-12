# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
  nums1.sort(); nums2.sort()
  answer=float("inf")
  for i in range(3):
   x=nums2[0]-nums1[i]; p=q=0
   while p<len(nums1) and q<len(nums2):
    if nums1[p]+x==nums2[q]:q+=1
    p+=1
   if q==len(nums2):answer=min(answer,x)
  return answer
