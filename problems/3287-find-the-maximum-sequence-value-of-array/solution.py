# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        size = len(nums)
        left = [set() for _ in range(size)]
        dp = [set() for _ in range(k + 1)]
        dp[0].add(0)
        for index, value in enumerate(nums):
            for count in range(min(k, index + 1), 0, -1):
                dp[count].update(previous | value for previous in dp[count - 1])
            left[index] = dp[k].copy()

        right = [set() for _ in range(size)]
        dp = [set() for _ in range(k + 1)]
        dp[0].add(0)
        for index in range(size - 1, -1, -1):
            value = nums[index]
            for count in range(min(k, size - index), 0, -1):
                dp[count].update(previous | value for previous in dp[count - 1])
            right[index] = dp[k].copy()

        answer = 0
        for split in range(k - 1, size - k):
            for first in left[split]:
                for second in right[split + 1]:
                    answer = max(answer, first ^ second)
        return answer
