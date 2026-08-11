# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:14Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        powers={bin(5**i)[2:] for i in range(7)}; n=len(s); dp=[n+1]*(n+1); dp[0]=0
        for i in range(n):
            for j in range(i+1,n+1):
                if s[i:j] in powers: dp[j]=min(dp[j],dp[i]+1)
        return dp[n] if dp[n]<=n else -1
