# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:27Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def minSumSquareDiff(
        self, nums1: List[int], nums2: List[int], k1: int, k2: int
    ) -> int:
        differences = [abs(first - second) for first, second in zip(nums1, nums2)]
        operations = k1 + k2
        if operations >= sum(differences):
            return 0

        low, high = 0, max(differences)
        while low < high:
            middle = (low + high) // 2
            required = sum(max(0, difference - middle) for difference in differences)
            if required <= operations:
                high = middle
            else:
                low = middle + 1

        level = low
        used = sum(max(0, difference - level) for difference in differences)
        remaining = operations - used
        total = sum(min(difference, level) ** 2 for difference in differences)
        return total - remaining * (2 * level - 1)
