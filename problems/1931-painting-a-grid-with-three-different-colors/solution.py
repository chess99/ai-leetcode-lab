# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        states=[]
        for value in range(3**m):
            row=[];x=value
            for _ in range(m):row.append(x%3);x//=3
            if all(row[i]!=row[i-1] for i in range(1,m)):states.append(row)
        compatible=[[j for j,b in enumerate(states) if all(x!=y for x,y in zip(a,b))] for a in states];dp=[1]*len(states);mod=1_000_000_007
        for _ in range(1,n):dp=[sum(dp[j] for j in compatible[i])%mod for i in range(len(states))]
        return sum(dp)%mod
