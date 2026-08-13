# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:37:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            middle = (left + right) // 2
            if arr[middle] < arr[middle + 1]:
                left = middle + 1
            else:
                right = middle
        return left
