# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:59:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for index, value in enumerate(nums):
            if index == value:
                return index
        return -1
