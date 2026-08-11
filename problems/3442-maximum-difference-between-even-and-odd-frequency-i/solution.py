# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:00:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxDifference(self, s: str) -> int:
        frequency = {}
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
        odd_max = max(count for count in frequency.values() if count % 2 == 1)
        even_min = min(count for count in frequency.values() if count % 2 == 0)
        return odd_max - even_min
