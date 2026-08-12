# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:02Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        dp=[0,0,0];mod=1_000_000_007
        for value in nums:
            if value==0:dp[0]=(2*dp[0]+1)%mod
            else:dp[value]=(2*dp[value]+dp[value-1])%mod
        return dp[2]
