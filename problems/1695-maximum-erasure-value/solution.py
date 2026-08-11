# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen=set();left=total=answer=0
        for value in nums:
            while value in seen:seen.remove(nums[left]);total-=nums[left];left+=1
            seen.add(value);total+=value;answer=max(answer,total)
        return answer
