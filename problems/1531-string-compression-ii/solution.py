# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:59Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dp(i,rem,last,count):
            if rem<0:return 10**9
            if i==len(s):return 0
            if s[i]==last:return (count in (1,9,99))+dp(i+1,rem,last,min(100,count+1))
            return min(1+dp(i+1,rem,s[i],1),dp(i+1,rem-1,last,count))
        return dp(0,k,'',0)
