# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:14Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod=10**9+7; dp=[0]*(n+1); dp[0]=1; base=1
        while (p:=base**x)<=n:
            for s in range(n,p-1,-1): dp[s]=(dp[s]+dp[s-p])%mod
            base+=1
        return dp[n]
