# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod=10**9+7;limit=14
        comb=[[0]*(limit+1)for _ in range(n+limit+1)]
        for i in range(len(comb)):
            comb[i][0]=1
            for j in range(1,min(i,limit)+1):comb[i][j]=(comb[i-1][j-1]+comb[i-1][j])%mod
        dp=[[0]*(maxValue+1)for _ in range(limit+1)]
        for x in range(1,maxValue+1):dp[1][x]=1
        ans=maxValue
        for length in range(2,limit+1):
            for x in range(1,maxValue+1):
                for y in range(x*2,maxValue+1,x):dp[length][y]=(dp[length][y]+dp[length-1][x])%mod
            ans=(ans+sum(dp[length]) * comb[n-1][length-1])%mod
        return ans
