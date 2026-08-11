# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n=len(nums); prime=[True]*n
        if n: prime[0]=False
        if n>1: prime[1]=False
        for i in range(2,int(n**.5)+1):
            if prime[i]: prime[i*i:n:i]=[False]*len(prime[i*i:n:i])
        a=sum(x for i,x in enumerate(nums) if prime[i]); return abs(a-(sum(nums)-a))
