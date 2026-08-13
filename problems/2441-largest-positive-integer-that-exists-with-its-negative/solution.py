# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:03:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        values = set(nums)
        return max((value for value in values if value > 0 and -value in values), default=-1)
