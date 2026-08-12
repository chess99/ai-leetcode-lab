# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:02Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod=10**9+7;dp=[[0]*(n+1)for _ in range(goal+1)];dp[0][0]=1
        for length in range(1,goal+1):
            for used in range(1,n+1):dp[length][used]=(dp[length-1][used-1]*(n-used+1)+dp[length-1][used]*max(0,used-k))%mod
        return dp[goal][n]
