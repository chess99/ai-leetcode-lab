# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        mod=10**9+7;ans=pre=0
        for x in sorted(nums):
            ans=(ans+x*x*(x+pre))%mod;pre=(2*pre+x)%mod
        return ans
