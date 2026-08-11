# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:27:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes=sum(all(value%d for d in range(2,int(value**.5)+1)) for value in range(2,n+1)); mod=10**9+7; result=1
        for value in range(2,primes+1): result=result*value%mod
        for value in range(2,n-primes+1): result=result*value%mod
        return result
