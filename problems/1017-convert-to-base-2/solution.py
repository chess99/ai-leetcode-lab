# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:10:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n==0:return '0'
        digits=[]
        while n:
            remainder = n & 1
            digits.append(str(remainder))
            n = (n - remainder) // -2
        return ''.join(reversed(digits))
