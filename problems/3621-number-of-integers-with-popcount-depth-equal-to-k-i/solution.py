# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:22Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0:return 1 if n >= 1 else 0
        bits=n.bit_length(); comb=[[0]*70 for _ in range(70)]
        for i in range(70):
            comb[i][0]=comb[i][i]=1
            for j in range(1,i):comb[i][j]=comb[i-1][j-1]+comb[i-1][j]
        dep=[0]*70
        for x in range(2,70):dep[x]=dep[x.bit_count()]+1
        def count(c):
            ans=0;need=c
            for i in range(bits-1,-1,-1):
                if n>>i&1:
                    if need<=i:ans+=comb[i][need]
                    need-=1
            return ans+(need==0)
        ans=sum(count(c) for c in range(1,bits+1) if dep[c]+1==k)
        return ans-(k==1)
