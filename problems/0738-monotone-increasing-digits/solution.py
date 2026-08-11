# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:41:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        marker = len(digits)
        for index in range(len(digits) - 1, 0, -1):
            if digits[index] < digits[index - 1]:
                digits[index - 1] = str(int(digits[index - 1]) - 1)
                marker = index
        for index in range(marker, len(digits)):
            digits[index] = "9"
        return int("".join(digits))
