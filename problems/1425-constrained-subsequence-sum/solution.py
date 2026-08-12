# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:54Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        candidates = deque()
        answer = nums[0]
        for index, value in enumerate(nums):
            while candidates and candidates[0] < index - k:
                candidates.popleft()
            dp[index] = value + max(0, dp[candidates[0]] if candidates else 0)
            while candidates and dp[candidates[-1]] <= dp[index]:
                candidates.pop()
            candidates.append(index)
            answer = max(answer, dp[index])
        return answer
