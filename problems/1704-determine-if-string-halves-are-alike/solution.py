# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:26:29Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU'); half = len(s) // 2
        return sum(ch in vowels for ch in s[:half]) == sum(ch in vowels for ch in s[half:])
