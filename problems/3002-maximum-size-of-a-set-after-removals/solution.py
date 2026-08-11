# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        first, second = set(nums1), set(nums2)
        limit = len(nums1) // 2
        only_first = len(first - second)
        only_second = len(second - first)
        shared = len(first & second)
        keep_first = min(limit, only_first)
        keep_second = min(limit, only_second)
        return keep_first + keep_second + min(shared, 2 * limit - keep_first - keep_second)
