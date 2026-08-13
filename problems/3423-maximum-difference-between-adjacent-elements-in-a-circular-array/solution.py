# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:59:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(a - b) for a, b in zip(nums, nums[1:] + nums[:1]))
