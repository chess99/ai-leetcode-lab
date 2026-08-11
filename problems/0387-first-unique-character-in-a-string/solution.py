# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:37:04Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        for index, char in enumerate(s):
            if counts[char] == 1:
                return index
        return -1
