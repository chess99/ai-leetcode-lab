# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        travenior = (nums1, nums2)
        base = sum(abs(a - b) for a, b in zip(nums1, nums2))
        target = nums2[-1]
        extra = min(
            0 if min(a, b) <= target <= max(a, b) else min(abs(a - target), abs(b - target))
            for a, b in zip(nums1, nums2)
        )
        return base + extra + 1
