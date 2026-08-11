# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:37:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        parts = ''.join(char if char.isdigit() else ' ' for char in word).split()
        return len({int(part) for part in parts})
