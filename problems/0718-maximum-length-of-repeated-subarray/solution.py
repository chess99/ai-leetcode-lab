# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:33:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        lengths = [0] * (len(nums2) + 1)
        longest = 0
        for first_number in nums1:
            for second_index in range(len(nums2) - 1, -1, -1):
                if first_number == nums2[second_index]:
                    lengths[second_index + 1] = lengths[second_index] + 1
                    longest = max(longest, lengths[second_index + 1])
                else:
                    lengths[second_index + 1] = 0
        return longest
