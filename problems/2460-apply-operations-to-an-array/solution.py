# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:03:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)-1):
            if nums[index]==nums[index+1]:nums[index]*=2;nums[index+1]=0
        values=[value for value in nums if value];return values+[0]*(len(nums)-len(values))
