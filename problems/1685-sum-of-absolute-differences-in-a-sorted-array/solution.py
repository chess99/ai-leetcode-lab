# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total=sum(nums);prefix=0;answer=[]
        for index,value in enumerate(nums):
            answer.append(value*index-prefix+(total-prefix-value)-value*(len(nums)-index-1));prefix+=value
        return answer
