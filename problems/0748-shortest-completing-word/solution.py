# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:59:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        required = {}
        for char in licensePlate.lower():
            if char.isalpha():
                required[char] = required.get(char, 0) + 1
        for word in sorted(words, key=len):
            counts = {}
            for char in word:
                counts[char] = counts.get(char, 0) + 1
            if all(counts.get(char, 0) >= count for char, count in required.items()):
                return word
