# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:04:24Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxFreqSum(self, s: str) -> int:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        vowels = set("aeiou")
        most_vowels = max((counts[char] for char in counts if char in vowels), default=0)
        most_consonants = max((counts[char] for char in counts if char not in vowels), default=0)
        return most_vowels + most_consonants
