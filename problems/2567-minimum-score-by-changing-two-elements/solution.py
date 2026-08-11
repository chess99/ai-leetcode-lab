# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(
            nums[-3] - nums[0],
            nums[-2] - nums[1],
            nums[-1] - nums[2],
        )
