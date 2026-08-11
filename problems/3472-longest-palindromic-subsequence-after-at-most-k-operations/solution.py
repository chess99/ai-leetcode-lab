# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:19Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache
class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(left,right,budget):
            if left>right:return 0
            if left==right:return 1
            best=max(dp(left+1,right,budget),dp(left,right-1,budget))
            diff=abs(ord(s[left])-ord(s[right])); cost=min(diff,26-diff)
            if cost<=budget: best=max(best,2+dp(left+1,right-1,budget-cost))
            return best
        return dp(0,len(s)-1,k)
