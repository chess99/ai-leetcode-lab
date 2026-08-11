# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:53:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        available = sorted(nums1)
        result = [0] * len(nums1)
        smallest, largest = 0, len(nums1) - 1
        for index in sorted(range(len(nums2)), key=nums2.__getitem__, reverse=True):
            if available[largest] > nums2[index]:
                result[index] = available[largest]
                largest -= 1
            else:
                result[index] = available[smallest]
                smallest += 1
        return result
