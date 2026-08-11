# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:23:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digits = [int(digit) for digit in str(n)]
        return sum(digit * digit for digit in digits) - sum(digits) >= 50
