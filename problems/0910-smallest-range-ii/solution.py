# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:58:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort(); answer=nums[-1]-nums[0]
        for i in range(len(nums)-1): answer=min(answer,max(nums[-1]-k,nums[i]+k)-min(nums[0]+k,nums[i+1]-k))
        return answer
