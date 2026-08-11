# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:24:15Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s>9*n:return -1
        if not s:return 0
        a=[]
        while s:a.append(str(min(9,s)));s-=min(9,s)
        return int(''.join(a)+'0'*(n-len(a)))
