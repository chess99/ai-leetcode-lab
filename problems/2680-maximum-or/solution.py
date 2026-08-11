# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        suffix=[0]*(len(nums)+1)
        for i in range(len(nums)-1,-1,-1): suffix[i]=suffix[i+1]|nums[i]
        answer=prefix=0
        for i,x in enumerate(nums): answer=max(answer,prefix|(x<<k)|suffix[i+1]); prefix|=x
        return answer
