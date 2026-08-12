# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s);dp=[0]*n
        for left in range(n-2,-1,-1):
            diagonal=0
            for right in range(left+1,n):
                old=dp[right]
                dp[right]=diagonal if s[left]==s[right] else min(dp[right],dp[right-1])+1
                diagonal=old
        return dp[-1]
