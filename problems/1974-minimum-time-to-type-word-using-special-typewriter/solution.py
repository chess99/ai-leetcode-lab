# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:56:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minTimeToType(self, word: str) -> int:
        total = len(word)
        current = 'a'
        for char in word:
            distance = abs(ord(char) - ord(current))
            total += min(distance, 26 - distance)
            current = char
        return total
