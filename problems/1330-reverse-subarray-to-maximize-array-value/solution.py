# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        if len(nums)<2:return 0
        base=sum(abs(a-b) for a,b in zip(nums,nums[1:]));gain=0
        for i in range(len(nums)-1):
            gain=max(gain,abs(nums[0]-nums[i+1])-abs(nums[i]-nums[i+1]),abs(nums[-1]-nums[i])-abs(nums[i]-nums[i+1]))
        low=max(min(a,b) for a,b in zip(nums,nums[1:]));high=min(max(a,b) for a,b in zip(nums,nums[1:]));gain=max(gain,2*(low-high))
        return base+gain
