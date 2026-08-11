# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:10:25Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        best_difference = nums[:]
        for left in range(len(nums) - 2, -1, -1):
            for right in range(left + 1, len(nums)):
                best_difference[right] = max(
                    nums[left] - best_difference[right],
                    nums[right] - best_difference[right - 1],
                )
        return best_difference[-1] >= 0
