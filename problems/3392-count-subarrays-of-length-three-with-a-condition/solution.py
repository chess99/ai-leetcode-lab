# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:59:23Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        return sum(2 * (nums[index] + nums[index + 2]) == nums[index + 1] for index in range(len(nums) - 2))
