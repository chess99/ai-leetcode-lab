# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:50:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = down = 1
        for previous, current in zip(nums, nums[1:]):
            if current > previous: up = down + 1
            elif current < previous: down = up + 1
        return max(up, down)
