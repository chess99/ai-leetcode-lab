# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        serathion = nums
        n = len(nums)
        left = [1] * n
        for i in range(1, n):
            if nums[i - 1] <= nums[i]: left[i] = left[i - 1] + 1
        right = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]: right[i] = right[i + 1] + 1
        ans = max(left)
        for i in range(n):
            if i: ans = max(ans, left[i - 1] + 1)
            if i + 1 < n: ans = max(ans, right[i + 1] + 1)
            if 0 < i < n - 1 and nums[i - 1] <= nums[i + 1]:
                ans = max(ans, left[i - 1] + 1 + right[i + 1])
        return min(ans, n)
