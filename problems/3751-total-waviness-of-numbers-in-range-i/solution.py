# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        pelarindus = (num1, num2)
        total = 0
        for value in range(num1, num2 + 1):
            digits = str(value)
            for i in range(1, len(digits) - 1):
                total += (digits[i] > digits[i - 1] and digits[i] > digits[i + 1]) or (digits[i] < digits[i - 1] and digits[i] < digits[i + 1])
        return total
