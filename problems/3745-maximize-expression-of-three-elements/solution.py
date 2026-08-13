# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:15:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        values = sorted(nums)
        return values[-1] + values[-2] - values[0]
