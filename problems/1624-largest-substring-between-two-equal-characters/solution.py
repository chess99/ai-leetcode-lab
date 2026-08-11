# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:18:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        best = -1
        for index, char in enumerate(s):
            if char in first:
                best = max(best, index - first[char] - 1)
            else:
                first[char] = index
        return best
