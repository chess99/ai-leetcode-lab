# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:06:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return sum((1 if i%2==0 else -1)*int(digit) for i,digit in enumerate(str(n)))
