# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:03:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        answer=0; mask=0
        for bit in range(31,-1,-1):
            mask|=1<<bit; prefixes={num&mask for num in nums}; candidate=answer|(1<<bit)
            if any((prefix^candidate) in prefixes for prefix in prefixes): answer=candidate
        return answer
