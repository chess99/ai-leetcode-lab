# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:42Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        torqavemin = (nums1, nums2)
        counts = Counter(nums1)
        counts.subtract(nums2)
        if any(delta & 1 for delta in counts.values()):
            return -1
        return sum(delta for delta in counts.values() if delta > 0) // 2
