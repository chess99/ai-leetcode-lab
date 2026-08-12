# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        mod=10**9+7;n=len(s)
        if k==0:return 1
        steps=[0]*(n+1)
        for i in range(2,n+1):steps[i]=steps[i.bit_count()]+1
        comb=[[0]*(n+1)for _ in range(n+1)]
        for i in range(n+1):
            comb[i][0]=comb[i][i]=1
            for j in range(1,i):comb[i][j]=(comb[i-1][j-1]+comb[i-1][j])%mod
        ans=0;ones=0
        for i,c in enumerate(s):
            if c=='1':
                remaining=n-i-1
                for q in range(ones,ones+remaining+1):
                    if steps[q]<k:ans=(ans+comb[n-i-1][q-ones])%mod
                ones+=1
        # The combinatorial scan also counts zero (zero set bits), while the
        # problem only asks for positive integers.
        return (ans-1)%mod
