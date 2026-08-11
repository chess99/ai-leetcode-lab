# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:04:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxProduct(self, n: int) -> int:
        digits = sorted((int(digit) for digit in str(n)), reverse=True)
        return digits[0] * digits[1]
