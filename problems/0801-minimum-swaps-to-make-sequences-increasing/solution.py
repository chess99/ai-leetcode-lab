# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        keep, swap = 0, 1
        for index in range(1, len(nums1)):
            next_keep = next_swap = len(nums1) + 1
            if nums1[index - 1] < nums1[index] and nums2[index - 1] < nums2[index]:
                next_keep = keep
                next_swap = swap + 1
            if nums1[index - 1] < nums2[index] and nums2[index - 1] < nums1[index]:
                next_keep = min(next_keep, swap)
                next_swap = min(next_swap, keep + 1)
            keep, swap = next_keep, next_swap
        return min(keep, swap)
