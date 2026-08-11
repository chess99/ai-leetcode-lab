# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        a=b=ans=1
        for i in range(1,len(nums1)):
            na=1+max(a if nums1[i]>=nums1[i-1] else 0,b if nums1[i]>=nums2[i-1] else 0)
            nb=1+max(a if nums2[i]>=nums1[i-1] else 0,b if nums2[i]>=nums2[i-1] else 0)
            a,b=na,nb; ans=max(ans,a,b)
        return ans
