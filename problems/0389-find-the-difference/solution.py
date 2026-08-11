# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:37:05Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        code = 0
        for char in s + t:
            code ^= ord(char)
        return chr(code)
