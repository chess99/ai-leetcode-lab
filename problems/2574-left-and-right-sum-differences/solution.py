# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:08:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right=sum(nums);left=0;result=[]
        for value in nums:right-=value;result.append(abs(left-right));left+=value
        return result
