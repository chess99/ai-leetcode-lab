# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        value=0;answer=[];mask=(1<<maximumBit)-1
        for number in nums:value^=number
        for number in reversed(nums):answer.append(value^mask);value^=number
        return answer
