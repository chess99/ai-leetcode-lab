# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:31:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        letters = set(s)
        for index, char in enumerate(s):
            if char.swapcase() not in letters:
                left = self.longestNiceSubstring(s[:index])
                right = self.longestNiceSubstring(s[index + 1:])
                return left if len(left) >= len(right) else right
        return s
