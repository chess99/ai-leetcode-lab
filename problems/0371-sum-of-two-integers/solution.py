# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:50:18Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=(1<<32)-1; maximum=(1<<31)-1
        while b:
            a,b=(a^b)&mask,((a&b)<<1)&mask
        return a if a<=maximum else ~(a^mask)
