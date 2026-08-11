# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        positive = nums[0]
        negative = float('-inf')
        for value in nums[1:]:
            positive, negative = max(positive, negative) + value, positive - value
        return int(max(positive, negative))
