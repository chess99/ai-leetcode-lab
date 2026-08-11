# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        answer = previous = current = 0
        for i, value in enumerate(nums):
            if i and nums[i - 1] >= value:
                answer = max(answer, current // 2, min(previous, current))
                previous, current = current, 1
            else:
                current += 1
        return max(answer, current // 2, min(previous, current))
