# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:31:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def secondHighest(self, s: str) -> int:
        digits=sorted({char for char in s if char.isdigit()}); return int(digits[-2]) if len(digits)>1 else -1
