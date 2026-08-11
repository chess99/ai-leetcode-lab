# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:05:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumSum(self, num: int) -> int:
        a,b,c,d=sorted(map(int,str(num)));return 10*a+10*b+c+d
