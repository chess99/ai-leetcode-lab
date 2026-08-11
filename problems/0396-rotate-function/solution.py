# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:52:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total=sum(nums); current=sum(i*x for i,x in enumerate(nums)); best=current
        for i in range(len(nums)-1,0,-1):
            current+=total-len(nums)*nums[i];best=max(best,current)
        return best
