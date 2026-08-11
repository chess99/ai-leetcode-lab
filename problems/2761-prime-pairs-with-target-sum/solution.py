# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime=[True]*(n+1); prime[0:2]=[False,False]
        for i in range(2,int(n**.5)+1):
            if prime[i]: prime[i*i:n+1:i]=[False]*len(range(i*i,n+1,i))
        return [[x,n-x] for x in range(2,n//2+1) if prime[x] and prime[n-x]]
