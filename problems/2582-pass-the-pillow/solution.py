# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:06:11Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        period=2*(n-1);position=time%period
        return position+1 if position<n else period-position+1
