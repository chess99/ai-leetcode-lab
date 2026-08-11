# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:51:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        return max(map(len, s.split('0'))) > max(map(len, s.split('1')))
