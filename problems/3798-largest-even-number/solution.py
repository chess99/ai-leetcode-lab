# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:16:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def largestEven(self, s: str) -> str:
        last = s.rfind('2')
        return s[:last + 1] if last != -1 else ''
