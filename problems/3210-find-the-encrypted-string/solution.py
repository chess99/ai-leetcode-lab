# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:45:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        shift = k % len(s)
        return s[shift:] + s[:shift]
