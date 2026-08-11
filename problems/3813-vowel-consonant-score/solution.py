# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:18:03Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = set("aeiou")
        vowel_count = sum(char in vowels for char in s)
        consonant_count = sum(char.isalpha() and char not in vowels for char in s)
        return vowel_count // consonant_count if consonant_count else 0
