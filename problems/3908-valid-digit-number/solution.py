# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:20:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        digits = str(n)
        target = str(x)
        return target in digits and digits[0] != target
