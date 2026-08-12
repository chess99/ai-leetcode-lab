# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:21Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from math import gcd


class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        answer=0; n=len(nums)
        for i in range(n):
            g=0; mn=100; need=0
            for j in range(i,n):
                g=gcd(g,nums[j]); v=(nums[j]&-nums[j]).bit_length()-1
                if v<mn: mn=v;need=1
                elif v==mn:need+=1
                # Doubling only raises GCD when every member has the same
                # minimum factor-of-two exponent; count those members.
                answer=max(answer,(j-i+1)*g*(2 if need<=k else 1))
        return answer
