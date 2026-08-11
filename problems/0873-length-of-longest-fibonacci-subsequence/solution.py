# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:53:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {value: position for position, value in enumerate(arr)}
        dp = [[2] * len(arr) for _ in arr]
        longest = 0
        for right in range(len(arr)):
            for middle in range(right):
                previous = arr[right] - arr[middle]
                if previous >= arr[middle] or previous not in index:
                    continue
                left = index[previous]
                dp[middle][right] = dp[left][middle] + 1
                longest = max(longest, dp[middle][right])
        return longest
