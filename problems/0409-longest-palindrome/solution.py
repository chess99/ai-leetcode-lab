# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:37:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = set()
        for char in s:
            if char in odd:
                odd.remove(char)
            else:
                odd.add(char)
        return len(s) - max(0, len(odd) - 1)
