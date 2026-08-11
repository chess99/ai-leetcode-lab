# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:08:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def scoreBalance(self, s: str) -> bool:
        total = sum(ord(char) - ord("a") + 1 for char in s)
        prefix = 0
        for char in s[:-1]:
            prefix += ord(char) - ord("a") + 1
            if prefix * 2 == total:
                return True
        return False
