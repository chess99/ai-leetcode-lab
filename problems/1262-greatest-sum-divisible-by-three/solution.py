# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:37:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]
        for value in nums:
            previous = dp[:]
            for remainder in range(3):
                dp[(remainder + value) % 3] = max(dp[(remainder + value) % 3], previous[remainder] + value)
        return dp[0]
