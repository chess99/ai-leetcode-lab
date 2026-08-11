# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:12:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [{} for _ in nums]
        answer = 2
        for right in range(len(nums)):
            for left in range(right):
                difference = nums[right] - nums[left]
                dp[right][difference] = max(
                    dp[right].get(difference, 0),
                    dp[left].get(difference, 1) + 1,
                )
                answer = max(answer, dp[right][difference])
        return answer
