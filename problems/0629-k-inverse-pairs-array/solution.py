# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:44Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod=10**9+7; dp=[1]+[0]*k
        for size in range(1,n+1):
            new=[0]*(k+1); run=0
            for j in range(k+1):
                run=(run+dp[j])%mod
                if j>=size: run=(run-dp[j-size])%mod
                new[j]=run
            dp=new
        return dp[k]
