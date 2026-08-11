# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        answer = 0
        for value in nums:
            remainder = value % k
            for total in range(k):
                previous = (total - remainder) % k
                dp[total][remainder] = max(dp[total][remainder], dp[total][previous] + 1)
                answer = max(answer, dp[total][remainder])
        return answer
