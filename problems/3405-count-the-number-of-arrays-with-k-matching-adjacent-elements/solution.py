# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:13Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod=10**9+7
        def pw(a,b):
            r=1
            while b:
                if b&1:r=r*a%mod
                a=a*a%mod;b//=2
            return r
        fact=[1]*(n+1)
        for i in range(1,n+1):fact[i]=fact[i-1]*i%mod
        return m*fact[n-1]*pw(fact[k]*fact[n-1-k]%mod,mod-2)%mod*pw(m-1,n-1-k)%mod
