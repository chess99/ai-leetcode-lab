# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1) + nums1.count(0), sum(nums2) + nums2.count(0)
        if sum1 == sum2:
            return sum1
        if sum1 < sum2 and 0 in nums1:
            return sum2
        if sum2 < sum1 and 0 in nums2:
            return sum1
        return -1
