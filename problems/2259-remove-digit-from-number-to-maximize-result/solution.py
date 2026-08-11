# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:18:37Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        return max(number[:i]+number[i+1:] for i,char in enumerate(number) if char==digit)
