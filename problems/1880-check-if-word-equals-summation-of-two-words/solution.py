# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:51:13Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def value(word):
            total = 0
            for char in word:
                total = total * 10 + ord(char) - ord('a')
            return total
        return value(firstWord) + value(secondWord) == value(targetWord)
