# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum = max(nums); best = run = 0
        for value in nums:
            run = run + 1 if value == maximum else 0
            best = max(best, run)
        return best
