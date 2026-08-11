# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:03:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = [int(word) for word in s.split() if word.isdigit()]
        return all(a < b for a, b in zip(numbers, numbers[1:]))
