# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:32Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        ordered=sorted(nums1);total=best=0
        for first,second in zip(nums1,nums2):
            difference=abs(first-second);total+=difference;index=bisect_left(ordered,second)
            for candidate in ordered[index:index+1]+ordered[max(0,index-1):index]:best=max(best,difference-abs(candidate-second))
        return (total-best)%(10**9+7)
