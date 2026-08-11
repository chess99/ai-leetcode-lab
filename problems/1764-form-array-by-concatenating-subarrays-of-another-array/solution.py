# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:28Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        start = 0
        for group in groups:
            while start + len(group) <= len(nums) and nums[start:start + len(group)] != group:
                start += 1
            if start + len(group) > len(nums):
                return False
            start += len(group)
        return True
