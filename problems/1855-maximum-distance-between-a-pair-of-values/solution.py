# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        first = second = answer = 0
        while first < len(nums1) and second < len(nums2):
            if nums1[first] <= nums2[second]: answer = max(answer, second - first); second += 1
            else: first += 1
        return answer
