# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:02:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(char) for char in s]
        while len(digits) > 2:
            digits = [(digits[index] + digits[index + 1]) % 10 for index in range(len(digits) - 1)]
        return digits[0] == digits[1]
