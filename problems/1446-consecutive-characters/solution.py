# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:58:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxPower(self, s: str) -> int:
        best = current = 1
        for i in range(1, len(s)):
            current = current + 1 if s[i] == s[i-1] else 1
            best = max(best, current)
        return best
