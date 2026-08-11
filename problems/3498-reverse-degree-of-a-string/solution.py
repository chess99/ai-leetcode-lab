# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:02:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((index + 1) * (26 - (ord(char) - ord('a'))) for index, char in enumerate(s))
