# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:22Z
# Experiment: ai-leetcode-lab, round 1

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        matched = 0
        for char in s:
            if matched == len(t):
                break
            if char == t[matched]:
                matched += 1
        return len(t) - matched
