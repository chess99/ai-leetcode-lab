# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        index = len(nums) - 1
        while index > 0 and nums[index - 1] < nums[index]:
            index -= 1
        return index
