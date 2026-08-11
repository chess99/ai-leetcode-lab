# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:25:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones=s.count('1');return '1'*(ones-1)+'0'*(len(s)-ones)+'1'
