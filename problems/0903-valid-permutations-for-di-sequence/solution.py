# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:01Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        mod=10**9+7;dp=[1]
        for ch in s:
            new=[0]*(len(dp)+1);run=0
            if ch=='I':
                for rank in range(1,len(new)):
                    run=(run+dp[rank-1])%mod;new[rank]=run
            else:
                for rank in range(len(dp)-1,-1,-1):
                    run=(run+dp[rank])%mod;new[rank]=run
            dp=new
        return sum(dp)%mod
