# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:14:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        positive=negative=answer=0
        for value in nums:
            if value==0: positive=negative=0
            elif value>0: positive,negative=positive+1,(negative+1 if negative else 0)
            else: positive,negative=(negative+1 if negative else 0),positive+1
            answer=max(answer,positive)
        return answer
