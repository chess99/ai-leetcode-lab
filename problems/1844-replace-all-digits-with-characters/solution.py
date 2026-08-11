# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:39:04Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def replaceDigits(self, s: str) -> str:
        chars = list(s)
        for i in range(1, len(chars), 2): chars[i] = chr(ord(chars[i-1]) + int(chars[i]))
        return ''.join(chars)
