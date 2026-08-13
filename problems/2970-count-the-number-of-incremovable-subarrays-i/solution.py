# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:39:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        result = 0
        for left in range(len(nums)):
            for right in range(left, len(nums)):
                remain = nums[:left] + nums[right+1:]
                result += all(a < b for a, b in zip(remain, remain[1:]))
        return result
