# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:58:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max=running_max=nums[0]; partition=0
        for i,value in enumerate(nums):
            running_max=max(running_max,value)
            if value<left_max: partition=i;left_max=running_max
        return partition+1
