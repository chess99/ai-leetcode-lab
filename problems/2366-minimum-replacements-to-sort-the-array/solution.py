# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans=0;limit=nums[-1]
        for x in nums[-2::-1]:
            parts=(x+limit-1)//limit;ans+=parts-1;limit=x//parts
        return ans
