# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:58:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums); current_max = current_min = best_max = best_min = nums[0]
        for value in nums[1:]:
            current_max = max(value, current_max + value); best_max = max(best_max, current_max)
            current_min = min(value, current_min + value); best_min = min(best_min, current_min)
        return best_max if best_max < 0 else max(best_max, total - best_min)
