# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        negative = -10 ** 18
        dp = [[negative] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for first_index, first in enumerate(nums1, 1):
            for second_index, second in enumerate(nums2, 1):
                product = first * second
                dp[first_index][second_index] = max(
                    dp[first_index - 1][second_index],
                    dp[first_index][second_index - 1],
                    product,
                    product + max(0, dp[first_index - 1][second_index - 1]))
        return dp[-1][-1]
