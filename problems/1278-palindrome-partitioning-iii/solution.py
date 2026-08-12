# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:47Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n=len(s);cost=[[0]*n for _ in range(n)]
        for length in range(2,n+1):
            for left in range(n-length+1):
                right=left+length-1
                cost[left][right]=(cost[left+1][right-1] if length>2 else 0)+(s[left]!=s[right])
        dp=[float('inf')]*(n+1);dp[0]=0
        for parts in range(1,k+1):
            following=[float('inf')]*(n+1)
            for end in range(parts,n+1):
                following[end]=min(dp[start]+cost[start][end-1] for start in range(parts-1,end))
            dp=following
        return dp[n]
