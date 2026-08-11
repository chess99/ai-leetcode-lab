# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort(); return sum(nums[len(nums)-2-2*i] for i in range(len(nums)//3))
