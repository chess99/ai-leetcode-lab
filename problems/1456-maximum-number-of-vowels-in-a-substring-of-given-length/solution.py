# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:51:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = sum(char in vowels for char in s[:k])
        best = count
        for index in range(k, len(s)):
            count += (s[index] in vowels) - (s[index - k] in vowels)
            best = max(best, count)
        return best
