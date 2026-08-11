# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:06Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort(); n=len(nums); answer=0
        for chosen in range(n+1):
            if (chosen==0 or nums[chosen-1]<chosen) and (chosen==n or chosen<nums[chosen]): answer+=1
        return answer
