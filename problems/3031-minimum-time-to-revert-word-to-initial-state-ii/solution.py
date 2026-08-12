# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n=len(word);z=[0]*n;l=r=0
        for i in range(1,n):
            if i<r:z[i]=min(r-i,z[i-l])
            while i+z[i]<n and word[z[i]]==word[i+z[i]]:z[i]+=1
            if i+z[i]>r:l,r=i,i+z[i]
        for i in range(k,n,k):
            if z[i]>=n-i:return i//k
        return (n+k-1)//k
