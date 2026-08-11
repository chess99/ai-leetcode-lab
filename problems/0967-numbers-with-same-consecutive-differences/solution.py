# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:05:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        values=list(range(1,10))
        for _ in range(n-1): values=[num*10+d for num in values for d in {num%10+k,num%10-k} if 0<=d<10]
        return values
