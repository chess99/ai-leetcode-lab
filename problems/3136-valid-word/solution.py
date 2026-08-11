# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:45:03Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isValid(self, word: str) -> bool:
        vowels = set("aeiouAEIOU")
        return (
            len(word) >= 3
            and word.isalnum()
            and any(char in vowels for char in word)
            and any(char.isalpha() and char not in vowels for char in word)
        )
