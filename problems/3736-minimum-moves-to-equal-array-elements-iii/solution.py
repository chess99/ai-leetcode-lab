# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:15:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)
        return sum(maximum - num for num in nums)
