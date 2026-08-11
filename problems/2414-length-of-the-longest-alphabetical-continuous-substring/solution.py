# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:15Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        best = current = 1
        for index in range(1, len(s)):
            current = current + 1 if ord(s[index]) == ord(s[index - 1]) + 1 else 1
            best = max(best, current)
        return best
