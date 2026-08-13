# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:57:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(value < k for value in nums):
            return -1
        return len({value for value in nums if value > k})
