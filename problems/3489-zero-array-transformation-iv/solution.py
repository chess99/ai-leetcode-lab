# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        possible=[1]*(len(nums))
        if all(value==0 for value in nums): return 0
        for step,(left,right,value) in enumerate(queries,1):
            bit=value
            for i in range(left,right+1): possible[i] |= possible[i]<<value
            if all((possible[i]>>nums[i])&1 for i in range(len(nums))): return step
        return -1
