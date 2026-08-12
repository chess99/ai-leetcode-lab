# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:45Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def strangePrinter(self, s: str) -> int:
        s=''.join(c for i,c in enumerate(s)if i==0 or c!=s[i-1]);n=len(s);dp=[[0]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i]=1
            for j in range(i+1,n):
                dp[i][j]=dp[i+1][j]+1
                for k in range(i+1,j+1):
                    if s[i]==s[k]:dp[i][j]=min(dp[i][j],dp[i+1][k-1]+dp[k][j])
        return dp[0][-1] if s else 0
