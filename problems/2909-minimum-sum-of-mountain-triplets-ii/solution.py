# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        right = [0] * len(nums)
        right[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])
        answer = float("inf")
        left = nums[0]
        for j in range(1, len(nums) - 1):
            if left < nums[j] and right[j + 1] < nums[j]:
                answer = min(answer, left + nums[j] + right[j + 1])
            left = min(left, nums[j])
        return -1 if answer == float("inf") else answer
