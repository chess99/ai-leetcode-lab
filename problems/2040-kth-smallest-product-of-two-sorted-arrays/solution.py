# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:05Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        from bisect import bisect_left,bisect_right
        def count(x):
            out=0
            for a in nums1:
                if a>0:out+=bisect_right(nums2,x//a)
                elif a<0:out+=len(nums2)-bisect_left(nums2,-((-x)//a))
                else:out+=len(nums2) if x>=0 else 0
            return out
        lo,hi=-10**10,10**10
        while lo<hi:
            mid=(lo+hi)//2
            if count(mid)>=k:hi=mid
            else:lo=mid+1
        return lo
