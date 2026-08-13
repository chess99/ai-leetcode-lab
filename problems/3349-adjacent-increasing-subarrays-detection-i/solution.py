# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:57:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for start in range(len(nums) - 2 * k + 1):
            first_increasing = all(nums[i] < nums[i + 1] for i in range(start, start + k - 1))
            second_increasing = all(nums[i] < nums[i + 1] for i in range(start + k, start + 2 * k - 1))
            if first_increasing and second_increasing:
                return True
        return False
