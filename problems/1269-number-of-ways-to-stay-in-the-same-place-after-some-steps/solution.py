# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:47Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod=1_000_000_007;size=min(arrLen,steps+1);dp=[0]*size;dp[0]=1
        for _ in range(steps):
            following=[0]*size
            for i,value in enumerate(dp):
                following[i]=(following[i]+value)%mod
                if i:following[i-1]=(following[i-1]+value)%mod
                if i+1<size:following[i+1]=(following[i+1]+value)%mod
            dp=following
        return dp[0]
