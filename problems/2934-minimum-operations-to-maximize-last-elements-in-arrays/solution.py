# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        def cost(last1, last2):
            changes = 0
            for a, b in zip(nums1[:-1], nums2[:-1]):
                if a <= last1 and b <= last2:
                    continue
                if b <= last1 and a <= last2:
                    changes += 1
                else:
                    return float("inf")
            return changes
        answer = min(cost(nums1[-1], nums2[-1]), cost(nums2[-1], nums1[-1]) + 1)
        return -1 if answer == float("inf") else answer
