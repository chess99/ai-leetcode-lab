# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:40:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = "-" if num < 0 else ""
        num = abs(num)
        digits = []
        while num:
            num, digit = divmod(num, 7)
            digits.append(str(digit))
        return sign + "".join(reversed(digits))
