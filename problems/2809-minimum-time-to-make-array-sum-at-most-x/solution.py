# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:42Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        size = len(nums1)
        dynamic = [0] * (size + 1)
        for first, second in sorted(zip(nums1, nums2), key=lambda pair: pair[1]):
            for operations in range(size, 0, -1):
                dynamic[operations] = max(dynamic[operations],
                                          dynamic[operations - 1]
                                          + first + operations * second)
        initial = sum(nums1)
        growth = sum(nums2)
        for operations in range(size + 1):
            if initial + operations * growth - dynamic[operations] <= x:
                return operations
        return -1
