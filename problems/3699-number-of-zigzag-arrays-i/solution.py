# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod=1_000_000_007;m=r-l+1
        up=[1]*m;down=[1]*m
        for _ in range(1,n):
            nu=[];s=0
            for x in range(m):nu.append(s);s=(s+down[x])%mod
            nd=[0]*m;s=0
            for x in range(m-1,-1,-1):nd[x]=s;s=(s+up[x])%mod
            up,down=nu,nd
        return (sum(up)+sum(down))%mod
