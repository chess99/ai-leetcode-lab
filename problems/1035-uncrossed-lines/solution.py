# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:12:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [0] * (len(nums2) + 1)
        for value1 in nums1:
            previous_diagonal = 0
            for index, value2 in enumerate(nums2, 1):
                previous_row_value = dp[index]
                if value1 == value2:
                    dp[index] = previous_diagonal + 1
                else:
                    dp[index] = max(dp[index], dp[index - 1])
                previous_diagonal = previous_row_value
        return dp[-1]
