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
        dp = [[1] * (k + 1) for _ in nums]
        answer = 1
        for right in range(len(nums)):
            for left in range(right):
                changed = nums[left] != nums[right]
                for used in range(changed, k + 1):
                    dp[right][used] = max(dp[right][used], dp[left][used - changed] + 1)
            answer = max(answer, max(dp[right]))
        return answer
