# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:08:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        digits = str(n)
        return [
            int(digit) * 10 ** (len(digits) - index - 1)
            for index, digit in enumerate(digits)
            if digit != "0"
        ]
