# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:46:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        prefix = [0]
        for number in nums: prefix.append(prefix[-1] + number)
        dp = [(prefix[-1] - prefix[i]) / (len(nums) - i) for i in range(len(nums))]
        for groups in range(2, k + 1):
            for start in range(len(nums) - groups + 1):
                dp[start] = max((prefix[end] - prefix[start]) / (end - start) + dp[end] for end in range(start + 1, len(nums) - groups + 2))
        return dp[0]
