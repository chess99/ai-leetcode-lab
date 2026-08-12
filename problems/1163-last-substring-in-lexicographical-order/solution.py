# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def lastSubstring(self, s: str) -> str:
        size = len(s)
        best, challenger, offset = 0, 1, 0
        while challenger + offset < size:
            if s[best + offset] == s[challenger + offset]:
                offset += 1
            elif s[best + offset] < s[challenger + offset]:
                best = max(best + offset + 1, challenger)
                challenger = best + 1
                offset = 0
            else:
                challenger += offset + 1
                offset = 0
        return s[best:]
