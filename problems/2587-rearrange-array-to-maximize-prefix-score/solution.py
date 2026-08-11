# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:27Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        total = score = 0
        for value in sorted(nums, reverse=True):
            total += value
            if total <= 0:
                break
            score += 1
        return score
