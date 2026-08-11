# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:14:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1
        while s[index] == " ":
            index -= 1

        length = 0
        while index >= 0 and s[index] != " ":
            length += 1
            index -= 1
        return length
