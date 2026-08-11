# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:53:15Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        return 1 if s == s[::-1] else 2
