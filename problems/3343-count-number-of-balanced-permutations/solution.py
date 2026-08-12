# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        from collections import Counter
        mod=10**9+7;n=len(num);half=n//2;total=sum(map(int,num))
        if total%2:return 0
        cnt=Counter(map(int,num));dp=[[0]*(total//2+1)for _ in range(half+1)];dp[0][0]=1
        fact=[1]*(n+1)
        for i in range(1,n+1):fact[i]=fact[i-1]*i%mod
        for d,c in cnt.items():
            nd=[[0]*(total//2+1)for _ in range(half+1)]
            for used in range(half+1):
                for sm in range(total//2+1):
                    if dp[used][sm]:
                        for q in range(min(c,half-used)+1):
                            if sm+d*q<=total//2:nd[used+q][sm+d*q]=(nd[used+q][sm+d*q]+dp[used][sm]*pow(fact[q]*fact[c-q]%mod,mod-2,mod))%mod
            dp=nd
        return dp[half][total//2]*fact[half]%mod*fact[n-half]%mod
