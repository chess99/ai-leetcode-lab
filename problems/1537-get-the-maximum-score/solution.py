# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:59Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = first = second = 0
        while i < len(nums1) or j < len(nums2):
            if j == len(nums2) or (i < len(nums1) and nums1[i] < nums2[j]): first += nums1[i]; i += 1
            elif i == len(nums1) or nums2[j] < nums1[i]: second += nums2[j]; j += 1
            else: first = second = max(first, second) + nums1[i]; i += 1; j += 1
        return max(first, second) % 1_000_000_007
