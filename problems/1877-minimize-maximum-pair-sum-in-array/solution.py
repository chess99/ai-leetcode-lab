# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[index] + nums[-1 - index] for index in range(len(nums) // 2))
