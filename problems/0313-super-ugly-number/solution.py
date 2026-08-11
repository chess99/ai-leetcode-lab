# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:47:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        values=[1]; indices=[0]*len(primes)
        while len(values)<n:
            next_value=min(primes[i]*values[indices[i]] for i in range(len(primes)))
            values.append(next_value)
            for i,p in enumerate(primes):
                while p*values[indices[i]]<=next_value: indices[i]+=1
        return values[-1]
