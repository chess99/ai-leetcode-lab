# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:05:57Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countDigits(self, num: int) -> int:
        return sum(digit != '0' and num % int(digit) == 0 for digit in str(num))
