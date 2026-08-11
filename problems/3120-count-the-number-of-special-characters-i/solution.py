# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:45:04Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)
        return sum(char in chars and char.upper() in chars for char in "abcdefghijklmnopqrstuvwxyz")
