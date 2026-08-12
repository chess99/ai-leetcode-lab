# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def distinctSequences(self, n: int) -> int:
        if n==1:return 6
        from math import gcd
        mod=10**9+7;dp=[[1 if gcd(i,j)==1 and i!=j else 0 for j in range(1,7)]for i in range(1,7)]
        for _ in range(2,n):
            nxt=[[0]*6 for _ in range(6)]
            for earlier in range(1,7):
                for previous in range(1,7):
                    for current in range(1,7):
                        if current!=earlier and current!=previous and gcd(previous,current)==1:
                            nxt[previous-1][current-1]=(nxt[previous-1][current-1]+dp[earlier-1][previous-1])%mod
            dp=nxt
        return sum(map(sum,dp))%mod
