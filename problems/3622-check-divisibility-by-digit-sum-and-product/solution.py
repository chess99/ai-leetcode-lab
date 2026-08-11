# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:04:43Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(char) for char in str(n)]
        digit_sum = sum(digits)
        product = 1
        for digit in digits:
            product *= digit
        return n % (digit_sum + product) == 0
