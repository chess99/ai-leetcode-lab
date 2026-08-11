# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:25Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1
        positive = negative = 0
        for a, b in zip(nums1, nums2):
            delta = a - b
            if delta % k:
                return -1
            if delta > 0:
                positive += delta // k
            else:
                negative -= delta // k
        return positive if positive == negative else -1
