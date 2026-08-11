# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:37:05Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for char in t:
            if index < len(s) and s[index] == char:
                index += 1
        return index == len(s)
