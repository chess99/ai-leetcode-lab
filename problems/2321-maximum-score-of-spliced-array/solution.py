# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def gain(a,b):
            cur=best=0
            for x,y in zip(a,b):cur=max(0,cur+y-x);best=max(best,cur)
            return best
        return max(sum(nums1)+gain(nums1,nums2),sum(nums2)+gain(nums2,nums1))
