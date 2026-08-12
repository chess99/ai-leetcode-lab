# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:28Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1)*6 < len(nums2) or len(nums2)*6 < len(nums1): return -1
        if sum(nums1) < sum(nums2): nums1, nums2 = nums2, nums1
        diff = sum(nums1)-sum(nums2); gains = sorted([value-1 for value in nums1]+[6-value for value in nums2],reverse=True)
        if diff == 0: return 0
        for count,gain in enumerate(gains,1):
            diff -= gain
            if diff <= 0: return count
        return -1
