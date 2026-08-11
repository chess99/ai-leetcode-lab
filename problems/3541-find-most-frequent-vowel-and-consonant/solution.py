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
        vowels = set('aeiou')
        return max((counts[char] for char in counts if char in vowels), default=0) + max((counts[char] for char in counts if char not in vowels), default=0)
