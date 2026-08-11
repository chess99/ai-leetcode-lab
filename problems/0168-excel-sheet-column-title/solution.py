# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:22:02Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chars = []
        while columnNumber:
            columnNumber -= 1
            chars.append(chr(ord("A") + columnNumber % 26))
            columnNumber //= 26
        return "".join(reversed(chars))
