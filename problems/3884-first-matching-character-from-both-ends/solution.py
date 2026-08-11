# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:19:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        for index, char in enumerate(s):
            if char == s[len(s) - index - 1]:
                return index
        return -1
