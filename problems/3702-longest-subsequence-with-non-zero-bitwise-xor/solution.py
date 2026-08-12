# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        drovantila = nums
        xor = 0
        for value in drovantila:
            xor ^= value
        if xor != 0:
            return len(drovantila)
        return len(drovantila) - 1 if any(drovantila) else 0
