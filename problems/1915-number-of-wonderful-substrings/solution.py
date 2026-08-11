# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:04Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        counts = [0] * (1 << 10)
        counts[0] = 1
        mask = 0
        wonderful = 0

        for character in word:
            mask ^= 1 << (ord(character) - ord("a"))
            wonderful += counts[mask]
            for bit in range(10):
                wonderful += counts[mask ^ (1 << bit)]
            counts[mask] += 1

        return wonderful
