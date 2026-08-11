# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:20Z
# Experiment: ai-leetcode-lab, round 1


class Solution:
    def countVowels(self, word: str) -> int:
        length = len(word)
        total = 0
        for index, char in enumerate(word):
            if char in "aeiou":
                total += (index + 1) * (length - index)
        return total
