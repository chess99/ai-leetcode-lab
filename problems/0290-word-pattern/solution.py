# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:31:05Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        char_to_word = {}
        word_to_char = {}
        for char, word in zip(pattern, words):
            if char_to_word.get(char, word) != word:
                return False
            if word_to_char.get(word, char) != char:
                return False
            char_to_word[char] = word
            word_to_char[word] = char
        return True
